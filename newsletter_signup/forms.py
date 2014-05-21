"""Forms for the ``newsletter_signup`` app."""
import uuid

from django import forms
from django.utils.translation import ugettext_lazy as _

from . import models


class NewsletterSignupForm(forms.ModelForm):
    """The form that handles the newsletter subscription."""

    def clean(self):
        cleaned_data = super(NewsletterSignupForm, self).clean()
        email = cleaned_data.get('email', None)
        if email is not None:
            if models.NewsletterSignup.objects.filter(email=email).exists():
                self._errors['email'] = [_(
                    'A subscription with this email already exists.')]
        cleaned_data['uuid'] = uuid.uuid4()
        return cleaned_data

    class Meta:
        model = models.NewsletterSignup
        fields = ['email', ]


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
