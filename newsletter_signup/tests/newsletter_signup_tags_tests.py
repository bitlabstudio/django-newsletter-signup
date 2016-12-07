"""Tests for the templatetags of the newsletter app."""
from django.test import TestCase, RequestFactory

from newsletter_signup.templatetags import newsletter_signup as tags


class HasSeenModalTestCase(TestCase):
    longMessage = True

    def test_tag(self):
        req = RequestFactory().get('/')
        req.session = {}
        context = {'request': req}
        tags.has_seen_modal(context)
        self.assertTrue(
            context['request'].session['has_seen_newsletter_signup_modal'],
            msg=('Should set the flag on the session to True'))
