# -*- coding: utf-8 -*-
from django.utils import timezone
from django.views.generic import FormView, View
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render_to_response

from braces.views import LoginRequiredMixin, GroupRequiredMixin
from allauth.account.adapter import get_adapter
from django.contrib import auth

from .forms import InviteForm
from .models import Invitation, InvitationsAdapter
from . import app_settings, signals


TEMPLATE_INVITATION  = 'invitations/forms/invite.html'
TEMPLATE_INVITATION_ACCEPTED = 'invitations/messages/invite_accepted.txt'
SUCCESS_MESSAGE = u'Ваше приглашение успешно отправлено адресату {email}'

class SendInvite(LoginRequiredMixin, FormView):
    template_name = TEMPLATE_INVITATION
    form_class = InviteForm

    def get_context_data( self, **kwargs ):
        ret = super(SendInvite, self).get_context_data(**kwargs)
        ret.update({ "username": auth.get_user(self.request).username })
        return ret

    def form_valid(self,form):
        email = form.cleaned_data["email"]
        try:
            user_id = auth.get_user(self.request).id
            invite = form.save(user_id)
            invite.send_invitation(self.request)
            invite.sent = timezone.now()
            invite.save()

        except Exception as e:
            return self.form_invalid(form)
        return self.render_to_response(
                    self.get_context_data(
                        success_message= SUCCESS_MESSAGE.format(email = email)))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

send_invitation = SendInvite.as_view()

class AcceptInvite(SingleObjectMixin, View):
    form_class = InviteForm

    def get(self, *args, **kwargs):
        if app_settings.CONFIRM_INVITE_ON_GET:
            return self.post(*args, **kwargs)
        else:
            raise Http404()

    def post(self, *args, **kwargs):
        self.object = invitation = self.get_object()
        invitation.accepted = True
        invitation.save()
        get_adapter().stash_verified_email(self.request, invitation.email)
        
        signals.invite_accepted.send(sender=self.request.user.__class__,
                                     request=self.request,
                                     email=invitation.email)

        get_adapter().add_message(self.request,
                                  messages.SUCCESS,
                                  TEMPLATE_INVITATION_ACCEPTED,
                                  {'email': invitation.email})
        return redirect(app_settings.SIGNUP_REDIRECT)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            return queryset.get(key=self.kwargs["key"].lower())
        except Invitation.DoesNotExist:
            raise Http404()

    def get_queryset(self):
        return Invitation.objects.all_valid()


accept_invitation = AcceptInvite.as_view()


