"""URLs for the newsletter_signup app."""
from django.conf.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^signup/$',
        views.NewsletterSignupView.as_view(),
        name='newsletter_signup'),
    re_path(r'^verify/(?P<uuid>.*)/',
        views.NewsletterVerifyView.as_view(),
        name='newsletter_verify'),
    re_path(r'^unsubscribe/$',
        views.NewsletterUnsubscribeView.as_view(),
        name='newsletter_unscubscribe'),
    re_path(r'^success/$',
        views.NewsletterSignupSuccessView.as_view(),
        name='newsletter_signup_success'),
]
