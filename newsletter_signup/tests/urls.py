"""URLs to run the tests."""
from django.conf.urls import include, url


urlpatterns = [
    url(r'^newsletter/', include('newsletter_signup.urls')),
]
