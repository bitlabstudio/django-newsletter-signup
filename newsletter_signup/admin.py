"""Admin classes for the newsletter_signup app."""
from django.contrib import admin

from . import models


class NewsletterSignupAdmin(admin.ModelAdmin):
    """Custom admin for the ``NewsletterSignup`` model."""
    list_display = ['email', 'user', 'signup_date', 'verification_date',
                    'verification_token']


admin.site.register(models.NewsletterSignup, NewsletterSignupAdmin)
