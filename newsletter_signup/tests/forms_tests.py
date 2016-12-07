"""Tests for the forms of the ``newsletter_signup`` app."""
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from mixer.backend.django import mixer
from unittest.case import skip

from .. import forms
from .. import models


# TODO: fix test with name params
@skip
class NewsletterSignupFormTestCase(TestCase):
    """Tests for the ``NewsletterSignupForm`` form class."""
    longMessage = True

    def get_request(self, data):
        request = RequestFactory().post(path='/', data=data)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        return request

    def setUp(self):
        self.data = {'email': 'user@example.com'}

    def test_form(self):
        request = self.get_request(self.data)
        form = forms.NewsletterSignupForm(request=request, data=self.data)
        self.assertTrue(form.is_valid(), msg=(
            'The form should be valid. Errors: {0}'.format(form.errors)))
        form.save()
        self.assertEqual(models.NewsletterSignup.objects.count(), 1, msg=(
            'There should be one subscription in the database.'))
        form = forms.NewsletterSignupForm(request=request, data=self.data)
        self.assertFalse(form.is_valid(), msg=(
            'When the subscription already exists, the form should not be'
            ' valid.'))

    def test_form_with_names(self):
        request = self.get_request(self.data)
        forms.NewsletterSignupForm.Meta.fields = [
            'email', 'first_name', 'last_name']
        form = forms.NewsletterSignupForm(request=request, data=self.data)
        self.assertFalse(form.is_valid(), msg=(
            'When the names are required, but not provided, the form'
            ' should not be valid'))

        data = self.data.copy()
        data.update({'first_name': 'Hans', 'last_name': 'Fooman'})
        request = self.get_request(data)
        form = forms.NewsletterSignupForm(request=request, data=data)
        self.assertTrue(form.is_valid(), msg=(
            'When the names are required, and provided correctly, the form'
            ' should be valid'))

    def test_settings_name_required(self):
        request = self.get_request(self.data)
        with self.settings(NEWSLETTER_SIGNUP_NAME_REQUIRED=True):
            form = forms.NewsletterSignupForm(request=request, data=self.data)
            self.assertTrue('first_name' in form.Meta.fields)
        with self.settings(NEWSLETTER_SIGNUP_NAME_REQUIRED=False):
            form = forms.NewsletterSignupForm(request=request, data=self.data)
            self.assertFalse('first_name' in form.Meta.fields)


class NewsletterUnsubscribeFormTestCase(TestCase):
    """Tests for the ``NewsletterUnsubscribeForm`` form class."""
    longMessage = True

    def setUp(self):
        self.subscription = mixer.blend('newsletter_signup.NewsletterSignup')
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
