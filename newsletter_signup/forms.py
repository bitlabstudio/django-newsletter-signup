"""Forms for the ``newsletter_signup`` app."""
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
        return cleaned_data

    class Meta:
        model = models.NewsletterSignup
        fields = ['email', ]
