"""URLs to run the tests."""
from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^newsletter/', include('newsletter_signup.urls')),
)
