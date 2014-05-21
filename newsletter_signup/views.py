"""Views for the newsletter_signup app."""
from django.utils.timezone import now
from django.views.generic import CreateView, TemplateView

from django_libs.utils_email import send_email

from . import forms
from . import models
from . import settings


class NewsletterSignupView(CreateView):
    """
    The view, where a user subscribes to the newsletter. Can also receive an
    AJAX request and answer with a partial.

    """
    form_class = forms.NewsletterSignupForm
    template_name = 'newsletter_signup/signup.html'
    ajax_template_name = 'newsletter_signup/ajax/signup.html'

    def form_valid(self, form):
        self.object = form.save()
        if callable(settings.SUBSCRIBE_SUBJECT):
            subject = settings.SUBSCRIBE_SUBJECT(self.object)
        else:  # pragma: nocover
            subject = settings.SUBSCRIBE_SUBJECT
        extra_context = {
            'subscription': self.object,
            'subject': subject,
        }
        send_email(
            self.request,
            extra_context,
            'newsletter_signup/email/subscribe_subject.html',
            'newsletter_signup/email/subscribe_body.html',
            settings.FROM_EMAIL,
            [self.object.email],
        )
        return self.render_to_response(self.get_context_data(
            form=form, subscription=self.object))

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.ajax_template_name]
        else:
            return [self.template_name]


class NewsletterUnsubscribeView(CreateView):
    """
    View to unsubscribe form a newsletter.

    """
    form_class = forms.NewsletterUnsubscribeForm
    template_name = 'newsletter_signup/unsubscribe.html'

    def form_valid(self, form):
        self.object = form.instance
        if callable(settings.UNSUBSCRIBE_SUBJECT):
            subject = settings.UNSUBSCRIBE_SUBJECT(self.object)
        else:  # pragma: nocover
            subject = settings.UNSUBSCRIBE_SUBJECT
        extra_context = {
            'subscription': self.object,
            'subject': subject,
        }
        send_email(
            self.request,
            extra_context,
            'newsletter_signup/email/unsubscribe_subject.html',
            'newsletter_signup/email/unsubscribe_body.html',
            settings.FROM_EMAIL,
            [self.object.email],
        )
        form.delete()
        return self.render_to_response(self.get_context_data(
            form=form, subscription_deleted=True))


class NewsletterVerifyView(TemplateView):
    """
    The view, where we check the verification token and set the subscription
    to active, if we can find it.

    """
    template_name = 'newsletter_signup/verify.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        uuid = kwargs.get('uuid')
        try:
            subscription = models.NewsletterSignup.objects.get(
                verification_token=uuid)
        except:
            context.update({'token_found': False, 'activated': False})
        else:
            context.update({'token_found': True})
            if subscription.verification_date is None:
                subscription.verification_date = now()
                subscription.save()
                context.update({'activated': True})
            else:
                context.update({'activated': False})
        return self.render_to_response(context)
