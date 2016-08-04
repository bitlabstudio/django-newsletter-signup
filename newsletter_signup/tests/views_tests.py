"""Tests for the views of the ``newsletter_signup`` app."""
from django.core.urlresolvers import reverse
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from mixer.backend.django import mixer

from .. import models
from .. import views


class NewsletterSignupViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``NewsletterSignupView`` view class."""
    view_class = views.NewsletterSignupView

    def get_view_name(self):
        return 'newsletter_signup'

    def setUp(self):
        self.data = {
            'email': 'email@example.com',
            'first_name': 'Foo',
            'last_name': 'Bar',
        }

    def test_view(self):
        self.is_callable()
        self.is_postable(data=self.data,
                         to=reverse('newsletter_signup_success'))
        self.assertEqual(models.NewsletterSignup.objects.count(), 1, msg=(
            'There should be one subscription in the database.'))
        self.post(data=self.data, ajax=True)
        self.data.update({'email': 'email2@example.com'})
        self.is_postable(data=self.data,
                         to=reverse('newsletter_signup_success'))
        self.assertEqual(models.NewsletterSignup.objects.count(), 2, msg=(
            'There should be two subscriptions in the database.'))
        self.data.update({'email': 'email3@example.com'})
        self.is_postable(ajax=True, data=self.data)
        self.assertEqual(models.NewsletterSignup.objects.count(), 3, msg=(
            'There should be three subscriptions in the database.'))


class NewsletterUnsubscribeViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``NewsletterUnsubscribeView`` view class."""
    view_class = views.NewsletterUnsubscribeView

    def get_view_name(self):
        return 'newsletter_unscubscribe'

    def setUp(self):
        self.subscription = mixer.blend('newsletter_signup.NewsletterSignup')
        self.data = {'email': self.subscription.email}

    def test_view(self):
        self.is_callable()
        resp = self.post(data=self.data)
        self.assert200(resp, msg=('The view should have been callable.'))
        self.assertEqual(models.NewsletterSignup.objects.count(), 0, msg=(
            'There should be no more subscription in the database.'))


class NewsletterVerifyViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``NewsletterVerifyView`` view class."""
    view_class = views.NewsletterVerifyView

    def get_view_kwargs(self):
        return {'uuid': self.subscription.verification_token}

    def setUp(self):
        self.subscription = mixer.blend('newsletter_signup.NewsletterSignup')

    def test_view(self):
        self.is_callable()
        self.assertEqual(models.NewsletterSignup.objects.filter(
            verification_date__isnull=False).count(), 1, msg=(
                'There should be one verified subscription in the db.'))
        # called with the same kwargs again
        self.is_callable()

        self.is_callable(kwargs={'uuid': 'wrong-uuid'})


class NewsletterSignupSuccessViewTestCase(ViewRequestFactoryTestMixin,
                                          TestCase):
    """Tests for the ``NewsletterSignupSuccessView`` view class."""
    view_class = views.NewsletterSignupSuccessView

    def test_view(self):
        self.is_callable()
