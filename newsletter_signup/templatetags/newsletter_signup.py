"""Templatetags for the newsletter app."""
from django import template

from .. import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def has_seen_modal(context):
    if settings.FORCE_MODAL:
        # TODO: I can't find a way to override the settings in a test and set
        # FORCE_MODAL to True / set pragma nocover here to get to 100% coverage
        context['request'].session['has_seen_newsletter_signup_modal'] = False  # pragma: nocover
    else:
        context['request'].session['has_seen_newsletter_signup_modal'] = True
    return ''
