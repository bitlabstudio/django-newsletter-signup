"""The models for the ``newsletter_signup`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import PostgreSQLUUIDField


class NewsletterSignup(models.Model):
    """
    Holds all information about a specific newsletter subscription.

    :user: The user, that has subscribed. None if anonymous.
    :email: The subscribed email.
    :signup_date: The date of the subscription.
    :verification_token: The unique token, that is required to verify the
      subscription.
    :verification_date: The date the token was used.

    """
    user = models.ForeignKey('auth.User', verbose_name=_('User'),
                             blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), max_length=64)
    signup_date = models.DateTimeField(verbose_name=_('Signup date'),
                                       auto_now_add=True)
    verification_token = PostgreSQLUUIDField(
        verbose_name=_('Verification token'))
    verification_date = models.DateTimeField(
        verbose_name=_('Verification date'), blank=True, null=True)

    def __unicode__(self):
        return self.email
