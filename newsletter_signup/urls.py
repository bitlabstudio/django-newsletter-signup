"""URLs for the newsletter_signup app."""
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^signup/$',
        views.NewsletterSignupView.as_view(),
        name='newsletter_signup'),
    url(r'^verify/(?P<uuid>.*)/',
        views.NewsletterVerifyView.as_view(),
        name='newsletter_verify'),
    url(r'^unsubscribe/$',
        views.NewsletterUnsubscribeView.as_view(),
        name='newsletter_unscubscribe'),
)
