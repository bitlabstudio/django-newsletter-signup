"""Tests for the models of the newsletter_signup app."""
from django.test import TestCase

from mixer.backend.django import mixer


class NewsletterSignupTestCase(TestCase):
    """Tests for the ``NewsletterSignup`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``NewsletterSignup`` model."""
        newslettersignup = mixer.blend('newsletter_signup.NewsletterSignup')
        self.assertTrue(newslettersignup.pk)
