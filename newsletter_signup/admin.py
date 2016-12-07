"""Admin classes for the newsletter_signup app."""
from django.contrib import admin

from . import models


class NewsletterSignupAdmin(admin.ModelAdmin):
    """Custom admin for the ``NewsletterSignup`` model."""
    list_display = [
        'email', 'first_name', 'last_name', 'source', 'referer',
        'current_referer', 'signup_date',
    ]
    list_filter = ['source', ]
    search_fields = ['source', 'email', 'first_name', 'last_name', ]


admin.site.register(models.NewsletterSignup, NewsletterSignupAdmin)
