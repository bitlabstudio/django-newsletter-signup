"""Forms for the ``newsletter_signup`` app."""
import uuid

from django import forms
from django.utils.translation import ugettext_lazy as _

from django_libs.utils.email import send_email

from . import models
from . import settings


if settings.NAME_REQUIRED:
    SIGNUP_FIELDS = ['first_name', 'last_name', 'email']
else:  # pragma: nocover
    SIGNUP_FIELDS = ['email', ]


class NewsletterSignupForm(forms.ModelForm):
    """The form that handles the newsletter subscription."""

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(NewsletterSignupForm, self).__init__(*args, **kwargs)
        self.source = request.session.get('initial_source', '')
        self.referer = request.session.get('initial_referer', '')
        self.current_referer = request.META.get('HTTP_REFERER', '')
        if settings.NAME_REQUIRED:
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.verification_required = settings.VERIFICATION_REQUIRED

    def clean_email(self):
        email = self.data.get('email', None)
        if email is not None:
            if models.NewsletterSignup.objects.filter(email=email).exists():
                raise forms.ValidationError(_(
                    'A subscription with this email already exists.'
                ))
        return email

    def save(self, *args, **kwargs):
        self.instance.source = self.source
        self.instance.referer = self.referer
        self.instance.current_referer = self.current_referer
        self.instance.verification_token = uuid.uuid4()
        self.instance = super(NewsletterSignupForm, self).save(*args, **kwargs)
        if settings.VERIFICATION_REQUIRED:
            # ATM this email only serves verification purposes and is not for
            # mere confirmation
            if callable(settings.SUBSCRIBE_SUBJECT):
                subject = settings.SUBSCRIBE_SUBJECT(self.instance)
            else:  # pragma: no cover
                subject = settings.SUBSCRIBE_SUBJECT
            extra_context = {
                'subscription': self.instance,
                'subject': subject,
            }
            send_email(
                self.request,
                extra_context,
                'newsletter_signup/email/subscribe_subject.html',
                'newsletter_signup/email/subscribe_body.html',
                settings.FROM_EMAIL,
                [self.instance.email],
            )
            return self.instance

    class Meta:
        model = models.NewsletterSignup
        fields = SIGNUP_FIELDS


class NewsletterUnsubscribeForm(forms.ModelForm):
    """Handles unsubscriptions from the newsletter."""

    def clean(self):
        cleaned_data = super(NewsletterUnsubscribeForm, self).clean()
        email = cleaned_data.get('email', None)
        if email is not None:
            try:
                self.instance = models.NewsletterSignup.objects.get(
                    email=email)
            except:
                self._errors['email'] = [_(
                    'A subscription with this email does not exist.')]
        return cleaned_data

    def delete(self):
        self.instance.delete()

    class Meta:
        model = models.NewsletterSignup
        fields = ['email', ]
