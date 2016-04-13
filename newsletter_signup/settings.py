"""Default settings for the ``newsletter_signup`` app."""
from django.conf import settings


def get_newsletter_signup_from_email():  # pragma: nocover
    try:
        email = getattr(settings, 'NEWSLETTER_SIGNUP_FROM_EMAIL',
                        settings.FROM_EMAIL)
    except AttributeError:
        raise NotImplementedError(
            'django-newsletter-signup requires ``FROM_EMAIL`` or'
            ' ``NEWSLETTER_SIGNUP_FROM_EMAIL`` to be defined.')
    return email


FROM_EMAIL = get_newsletter_signup_from_email()

# Both subject settings can also be a callable object receiving the
# newslettersubscription instance
SUBSCRIBE_SUBJECT = getattr(
    settings, 'NEWSLETTER_SIGNUP_SUBSCRIBE_SUBJECT',
    'Thanks for subscribing to our newsletter')

UNSUBSCRIBE_SUBJECT = getattr(
    settings, 'NEWSLETTER_SIGNUP_UNSUBSCRIBE_SUBJECT',
    'You\'ve been unsubscribed from our newsletter')

VERIFICATION_REQUIRED = getattr(
    settings,
    'NEWSLETTER_SIGNUP_VERIFICATION_REQUIRED',
    False
)

NAME_REQUIRED = getattr(
    settings,
    'NEWSLETTER_SIGNUP_NAME_REQUIRED',
    False
)

DOMAIN = getattr(
    settings,
    'DOMAIN',
    'localhost:8000'
)

FORCE_MODAL = getattr(
    settings,
    'NEWSLETTER_SIGNUP_FORCE_MODAL',
    False,
)
