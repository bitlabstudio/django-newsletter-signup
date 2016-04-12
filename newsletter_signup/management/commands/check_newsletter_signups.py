"""Custom admin command to check all newsletter signups."""
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from newsletter_signup.models import NewsletterSignup


class Command(BaseCommand):
    """
    Tries to match NewsletterSignups, that don't have a user with the users
    in the database.

    """
    def handle(self, **options):
        resolved = 0
        signups = NewsletterSignup.objects.filter(user__isnull=True)
        user_model = get_user_model()
        for signup in signups:
            try:
                signup.user = user_model.objects.get(email=signup.email)
            except ObjectDoesNotExist:
                continue
            resolved += 1
            signup.save()
        print('{} of {} signups resolved.'.format(resolved, signups.count()))
