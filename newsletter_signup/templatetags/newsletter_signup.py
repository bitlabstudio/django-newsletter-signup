"""Templatetags for the newsletter app."""
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def has_seen_modal(context):
    if getattr(settings, 'NEWSLETTER_FORCE_MODAL', False):
        return ''
    context['request'].session['has_seen_newsletter_signup_modal'] = True
    return ''
