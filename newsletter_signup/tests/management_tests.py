"""Tests for the management commands of the ``newsletter_signup`` app."""
from django.core.management import call_command
from django.test import TestCase

from django_libs.tests.factories import UserFactory

from .factories import NewsletterSignupFactory
from ..models import NewsletterSignup


class CheckNewsletterSignupsTestCase(TestCase):
    """Tests for the ``check_newsletter_signups`` management command."""
    longMessage = True

    def test_reminder(self):
        signup = NewsletterSignupFactory()
        call_command('check_newsletter_signups')
        self.assertIsNone(NewsletterSignup.objects.all()[0].user, msg=(
            'No user should be assigned.'))

        user = UserFactory(email=signup.email)
        call_command('check_newsletter_signups')
        self.assertEqual(NewsletterSignup.objects.all()[0].user, user, msg=(
            'User instance should have been assigned.'))
