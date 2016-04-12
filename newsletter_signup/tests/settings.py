"""
These settings are used by the ``manage.py`` command.

With normal tests we want to use the fastest possible way which is an
in-memory sqlite database, but if you want to create migrations you need a
persistent database.

"""
from .test_settings import *  # NOQA


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}
