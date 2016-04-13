Django Newsletter Signup
========================

A reusable Django app, that handles newsletter subscriptions.

Important note!
+++++++++++++++

If you upgrade from 0.2 upwards, you need to be aware, that the migrations were
reset. They used to be south, but they have been re-created to new Django
migrations in 0.3.

If you're first install is on 0.3 or beyond, you don't have to do anything.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-newsletter-signup

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-newsletter-signup.git#egg=newsletter_signup

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
        url(r'^newsletter/', include('newsletter_signup.urls')),
    )

Add the provided middleware to catch all referrers

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        '...',  # your other middlewares
        'newsletter.middleware.GetRefererMiddleware',
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate newsletter_signup


Usage
-----

Just link to the signup page or fetch it's contents via AJAX into e.g. a
bootstrap modal. Once a user fills out the subscription form she gets a
verification email, that on click makes the Subscription verified.

Future updates might include mailchimp integration to have everything setup
right away. For now you then need to gather the emails from the admin or your
own custom management views that you want to send mails to, or alternatively
create a custom management command.

Management Commands
-------------------

check_newsletter_signups
++++++++++++++++++++++++

This command will iterate through all signups and check if there's a user in
the system matching a signup's email. You might want to run this command in a
cron job.

Settings
--------

DOMAIN
++++++

``Default = 'locahost:8000'``

``DOMAIN`` is the hostname of your site.

.. code-block:: python

    DOMAIN = 'example.com'

NEWSLETTER_SIGNUP_FROM_EMAIL
++++++++++++++++++++++++++++

To set the from email in the mails, you can either specifically set the
``NEWSLETTER_SIGNUP_FROM_EMAIL`` setting or only the ``FROM_EMAIL`` setting,
which it per default falls back to.

..code-block:: python

    NEWSLETTER_SIGNUP_FROM_EMAIL = 'news@example.com'


NEWSLETTER_SIGNUP_SUBSCRIBE_SUBJECT and NEWSLETTER_SIGNUP_UNSUBSCRIBE_SUBJECT
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Both of these setting work in the same way as they set the email subject for
the subscripe and unsubscribe email. You can either provide a string or a
callable object receiving the subscription object as a parameter.
See ``models.py`` for details. Alternatively you could overwrite those two
templates ``email/unsubscripe_subject.html`` and
``email/subscripe_subject.html``.

..code-block:: python

    SUBSCRIBE_SUBJECT = 'Your subscription to our newsletter!'

    UNSUBSCRIBE_SUBJECT = lambda sub: '{0} was unsubscribed.'.format(
        sub.email)


NEWSLETTER_SIGNUP_FORCE_MODAL
+++++++++++++++++++++++++++++

``Default = False``

If you use a modal or some other kind of visual element, to hint at the
newsletter, you can set this to True to always show it.

It's intended, that you do something like this in your template::

    {% if not request.session.has_seen_newsletter_signup_modal %}
        {% has_seen_modal %}
        {% include "path/to/newsletter_signup_modal.html" %}
    {% endif %}

The ``has_seen_modal`` template tag sets the session value
``has_seen_newsletter_signup_modal`` to ``True`` when the tag is rendered.

That way, the user won't see the modal the next time the view is called, unless
you set ``NEWSLETTER_SIGNUP_FORCE_MODAL`` to ``True``, since that prevents the
session value from becoming ``True`` in the first place.

NEWSLETTER_SIGNUP_NAME_REQUIRED
+++++++++++++++++++++++++++++++

``Default = False``

If set to ``True`` this setting will add ``first_name`` and ``last_name`` fields
to the signup form. These values are then stored on the ``NewsletterSignup``
model.

NEWSLETTER_SIGNUP_VERIFICATION_REQUIRED
+++++++++++++++++++++++++++++++++++++++

``Default = False``

If set to ``True`` the user will receive an email after signing up with a
verification link.
Same goes for unsubscription.
Per default the user is just (un)subscribed on form submit.


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
