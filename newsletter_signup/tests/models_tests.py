"""Tests for the models of the newsletter_signup app."""
from django.test import TestCase

from . import factories


class NewsletterSignupTestCase(TestCase):
    """Tests for the ``NewsletterSignup`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``NewsletterSignup`` model."""
        newslettersignup = factories.NewsletterSignupFactory()
        self.assertTrue(newslettersignup.pk)
