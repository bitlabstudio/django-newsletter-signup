"""Tests for the forms of the ``newsletter_signup`` app."""
from django.test import TestCase

from . import factories
from .. import forms
from .. import models


class NewsletterSignupFormTestCase(TestCase):
    """Tests for the ``NewsletterSignupForm`` form class."""
    longMessage = True

    def setUp(self):
        self.data = {'email': 'user@example.com'}

    def test_form(self):
        form = forms.NewsletterSignupForm(self.data)
        self.assertTrue(form.is_valid(), msg=(
            'The form should be valid. Errors: {0}'.format(form.errors)))
        form.save()
        self.assertEqual(models.NewsletterSignup.objects.count(), 1, msg=(
            'There should be one subscription in the database.'))
        form = forms.NewsletterSignupForm(self.data)
        self.assertFalse(form.is_valid(), msg=(
            'When the subscription already exists, the form should not be'
            ' valid.'))


class NewsletterUnsubscribeFormTestCase(TestCase):
    """Tests for the ``NewsletterUnsubscribeForm`` form class."""
    longMessage = True

    def setUp(self):
        self.subscription = factories.NewsletterSignupFactory()
        self.data = {'email': self.subscription.email}

    def test_form(self):
        form = forms.NewsletterUnsubscribeForm({'email': 'wrong@example.com'})
        self.assertFalse(form.is_valid(), msg=(
            'When the email is not found on a subscription, the form should'
            ' not be valid.'))

        form = forms.NewsletterUnsubscribeForm(self.data)
        self.assertTrue(form.is_valid(), msg=(
            'The form should be valid. Errors: {0}'.format(form.errors)))
        form.delete()
        self.assertEqual(models.NewsletterSignup.objects.count(), 0, msg=(
            'There should be no subscription in the database.'))
