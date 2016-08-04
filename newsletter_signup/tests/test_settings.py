# flake8: noqa
"""Settings that need to be set in order to run the tests."""
import logging
import os

DEBUG = True

logging.getLogger("factory").setLevel(logging.WARN)

SITE_ID = 1

DOMAIN = 'localhost:8000'
PROTOCOL = 'http'

APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'newsletter_signup.tests.urls'

FROM_EMAIL = 'from@example.com'
EMAIL_SUBJECT_PREFIX = '[test cremesimon] '
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_ROOT, '../app_static')
MEDIA_ROOT = os.path.join(APP_ROOT, '../app_media')
STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [os.path.join(APP_ROOT, 'tests/test_app/templates'),],
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.i18n',
            'django.template.context_processors.request',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
        )
    }
}]

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.join(APP_ROOT, 'tests/coverage'))
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
]

INTERNAL_APPS = [
    'newsletter_signup',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

SECRET_KEY = 'foobar'


NEWSLETTER_SIGNUP_SUBSCRIBE_SUBJECT = lambda sub: 'User {0} subscribed'.format(
    sub.user or sub.email)
NEWSLETTER_SIGNUP_UNSUBSCRIBE_SUBJECT = lambda sub: 'User {0} unsubscribed'.format(
    sub.user or sub.email)
NEWSLETTER_SIGNUP_VERIFICATION_REQUIRED = True
NEWSLETTER_SIGNUP_NAME_REQUIRED = True
