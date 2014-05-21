"""Factories for the newsletter_signup app."""
import factory

from .. import models


class NewsletterSignupFactory(factory.DjangoModelFactory):
    """Factory for the ``NewsletterSignup`` model."""
    FACTORY_FOR = models.NewsletterSignup

    email = factory.Sequence(lambda n: 'email{0}@example.com'.format(n))
