"""Tests for the middlewares of the newsletter app."""
from django.test import TestCase, RequestFactory

from .. import middleware


class GetRefererMiddlewareTestCase(TestCase):
    longMessage = True

    def test_middleware(self):
        req = RequestFactory().get('/')
        req.session = {}
        referer = 'https://google.com'
        req.META['HTTP_REFERER'] = referer
        middleware.GetRefererMiddleware().process_request(req)
        self.assertEqual(req.session['initial_referer'], referer, msg=(
            'Should set the initial referer'))

        new_referer = 'http://localhost:8000/bla'
        req.META['HTTP_REFERER'] = new_referer
        middleware.GetRefererMiddleware().process_request(req)
        self.assertEqual(req.session['initial_referer'], referer, msg=(
            'Should not set the new referer when it is an internal one'))

        new_referer = 'http://bing.com'
        req.META['HTTP_REFERER'] = new_referer
        middleware.GetRefererMiddleware().process_request(req)
        self.assertEqual(req.session['initial_referer'], new_referer, msg=(
            'Should not set the new referer when it is an external one'))
