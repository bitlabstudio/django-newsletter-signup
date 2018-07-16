"""The models for the ``newsletter_signup`` app."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class NewsletterSignup(models.Model):
    """
    Holds all information about a specific newsletter subscription.

    :user: The user, that has subscribed. None if anonymous.
    :first_name: First name of the user, that has subscribed. Takes precedence
      over user.first_name.
    :last_name: Last name of the user, that has subscribed. Takes precedence
      over user.last_name.
    :email: The subscribed email. Takes precedence of the user.email.
    :signup_date: The date of the subscription.
    :source: Encoded GET arguments. Let's you store e.g. campaign specific
      information.
    :referer: HTTP referer when the user visited the site for the first time.
      This can often be empty when the user came from secure sites or their
      client is surpressing the HTTP referer.
    :current_referer: HTTP referer at the moment when the user submits the
      form. This can often be your own site because the user might have
      browsed around for a while before submitting the form.
    :verification_token: The unique token, with which a user verifies her
      subscription. Only required if verification setting is True.
    :verification_date: The date the token was used.

    Note: The user fields should only be used as initial values, the actual
      name and email values are stored directly here.

    """
    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('user'),
        blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(
        max_length=512, blank=True, verbose_name=_('first name'), )
    last_name = models.CharField(
        max_length=512, blank=True, verbose_name=_('last name'))
    email = models.EmailField(max_length=1024, verbose_name=_('email'))
    signup_date = models.DateTimeField(
        verbose_name=_('signup date'), auto_now_add=True)

    source = models.CharField(max_length=1024, blank=True, null=True)
    referer = models.CharField(
        max_length=2048, blank=True, verbose_name=_('Initial referer')
    )
    current_referer = models.CharField(max_length=2048, blank=True)

    verification_token = models.UUIDField(
        verbose_name=_('Verification token'), blank=True, null=True)
    verification_date = models.DateTimeField(
        verbose_name=_('Verification date'), blank=True, null=True)

    # COMPATIBILITY CODE FOR RENAMED FIELDS
    # Use signup_date instead!
    @property
    def creation_date(self):  # pragma: nocover
        return self.signup_date

    @creation_date.setter
    def creation_date(self, value):  # pragma: nocover
        self.signup_date = value

    @creation_date.deleter
    def creation_date(self):  # pragma: nocover
        self.signup_date = None

    # END COMPATIBILITY CODE

    def __str__(self):  # pragma: nocover
        return self.email
