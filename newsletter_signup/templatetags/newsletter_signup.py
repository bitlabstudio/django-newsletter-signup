"""Templatetags for the newsletter app."""
from django import template

from .. import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def has_seen_modal(context):
    if getattr(settings, 'FORCE_MODAL', False):
        context['request'].session['has_seen_newsletter_signup_modal'] = False
    else:
        context['request'].session['has_seen_newsletter_signup_modal'] = True
    return ''
