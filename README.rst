Django Newsletter Signup
============

A reusable Django app, that handles newsletter subscriptions.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-newsletter-signup

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-newsletter-signup.git#egg=newsletter_signup

TODO: Describe further installation steps (edit / remove the examples below):

Add ``newsletter_signup`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'newsletter_signup',
    )

Add the ``newsletter_signup`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^newsletter-signup/', include('newsletter_signup.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load newsletter_signup_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate newsletter_signup


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-newsletter-signup
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
