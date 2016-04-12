"""Middlewares for the newsletter_signup app."""
import re

from . import settings


class GetRefererMiddleware(object):
    def process_request(self, request):
        referer = request.META.get('HTTP_REFERER')
        pattern = r'https?://{0}'.format(settings.DOMAIN)
        if referer and re.match(pattern=pattern, string=referer):
            return
        request.session['initial_referer'] = referer
