# -*- coding: utf-8 -*-
from django import forms
from allauth.account.forms import AddEmailForm
import re
from django.forms import ModelForm
from invitations.models import Invitation
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from allauth.account.adapter import get_adapter
from django.utils import timezone
import signals

class InviteForm(ModelForm):
    class Meta:
        model = Invitation
        fields = ['email']

    def clean_email( self ):
        errors = {
            "already_invited": u"На этот адрес ранее уже было отправлено приглашение.",
            "wrong_format": u'Введите правильный email!'
        }
        email = self.cleaned_data['email']
        if (len(email) < 6) or (not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email)):
            raise forms.ValidationError(errors["wrong_format"])
        if Invitation.objects.filter(email__iexact=email,
                                     accepted=False):
            raise forms.ValidationError(errors["already_invited"])

        return email

    def save(self, user_id):
        return Invitation.create(email=self.instance.email, user_id=user_id)

