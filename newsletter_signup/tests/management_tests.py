"""Tests for the management commands of the ``newsletter_signup`` app."""
from django.core.management import call_command
from django.test import TestCase

from mixer.backend.django import mixer

from ..models import NewsletterSignup


class CheckNewsletterSignupsTestCase(TestCase):
    """Tests for the ``check_newsletter_signups`` management command."""
    longMessage = True

    def test_reminder(self):
        signup = mixer.blend('newsletter_signup.NewsletterSignup')
        call_command('check_newsletter_signups')
        self.assertIsNone(NewsletterSignup.objects.all()[0].user, msg=(
            'No user should be assigned.'))

        user = mixer.blend('auth.User', email=signup.email)
        call_command('check_newsletter_signups')
        self.assertEqual(NewsletterSignup.objects.all()[0].user, user, msg=(
            'User instance should have been assigned.'))
