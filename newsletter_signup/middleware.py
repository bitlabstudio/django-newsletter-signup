"""Middlewares for the newsletter_signup app."""


class GetRefererMiddleware(object):
    def process_request(self, request):
        referer = request.META.get('HTTP_REFERER')
        if request.session.get('initial_referer') is None:
            request.session['initial_referer'] = referer and referer or ''
            pass
        if request.session.get('initial_source') is None:
            source = request.GET.urlencode()
            request.session['initial_source'] = source and source or ''
            pass
