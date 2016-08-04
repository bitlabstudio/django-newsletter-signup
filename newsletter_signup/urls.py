"""URLs for the newsletter_signup app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/$',
        views.NewsletterSignupView.as_view(),
        name='newsletter_signup'),
    url(r'^verify/(?P<uuid>.*)/',
        views.NewsletterVerifyView.as_view(),
        name='newsletter_verify'),
    url(r'^unsubscribe/$',
        views.NewsletterUnsubscribeView.as_view(),
        name='newsletter_unscubscribe'),
    url(r'^success/$',
        views.NewsletterSignupSuccessView.as_view(),
        name='newsletter_signup_success'),
]
