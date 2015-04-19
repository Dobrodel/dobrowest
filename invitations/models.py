# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.core.validators import validate_email

from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.adapter import get_adapter
from accounts.models import CustomUser

from managers import InvitationManager
import app_settings
import signals

TEMPLATE_EMAIL = 'invitations/email/email_invite'

#@python_2_unicode_compatible
class Invitation(models.Model):
    class Meta:
        db_table = "dobro_invitations"
        verbose_name = u'Приглашение'
        verbose_name_plural = u"Приглашения"

    email = models.EmailField(verbose_name = "E-mail адресата",
                              blank = False, unique = True,
                              validators = [validate_email],
                              help_text = 'Введите пожалуйста email адресата',
                              )
    accepted = models.BooleanField(verbose_name=u'Код принят', default=False)
    created = models.DateTimeField(verbose_name = "Дата создания", auto_now_add = True)
    key = models.CharField(verbose_name=u'Код приглашения', max_length=64, unique=True)
    sent = models.DateTimeField(verbose_name=u'Дата отправки', null=True)
    user = models.ForeignKey(CustomUser, verbose_name = "Приглашающий")

    objects = InvitationManager()

    @classmethod
    def create(cls, email, user_id):
        key = get_random_string(64).lower()
        user=CustomUser.objects.get(id = user_id)
        instance = cls._default_manager.create(
            email=email,
            key=key,
            user=user)
        return instance

    def key_expired(self):
        expiration_date = (
            self.sent + datetime.timedelta(
                days=app_settings.INVITATION_EXPIRY))
        return expiration_date <= timezone.now()
    key_expired.boolean = True

    def send_invitation(self, request, **kwargs):
        current_site = (kwargs['site'] if 'site' in kwargs
                        else Site.objects.get_current())
        invite_url = reverse('accept-invitation',
                             args=[self.key])
        invite_url = request.build_absolute_uri(invite_url)

        ctx = {
            'invite_url': invite_url,
            'current_site': current_site,
            'email': self.email,
            'key': self.key,
        }

        get_adapter().send_mail(TEMPLATE_EMAIL,
                                self.email,
                                ctx)
        self.sent = timezone.now()
        self.save()
        signals.invite_url_sent.send(
            sender=self.__class__,
            instance=self,
            invite_url_sent=invite_url)

    def __unicode__(self):
        return u"Адресат: {}".format(self.email)


class InvitationsAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        if request.session.get('account_verified_email'):
            mail = request.session.get('account_verified_email')
            self.stash_verified_email(request, mail)
            return True
        elif app_settings.INVITATION_ONLY is True:
            # Site is ONLY open for invites
            return False
        else:
            # Site is open to signup
            return True

