# -*- coding: utf-8 -*-
__author__ = 'adam'
#
# -----------------------------------------------------
#   
# Проект: vsekdobru
#   Имя файла: forms.py
#   Дата создания: 10.04.15 
#   Время создания: 6:43
#   Автор проекта: adam
#
#-----------------------------------------------------
#
#from django import forms
from django.contrib.auth.forms import UserChangeForm

from accounts.models import CustomUser

#from allauth.account.forms import SetPasswordField, PasswordField
#from invitations.models import Invitations

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

'''
#
#   Переопределяю форму Регистрации модуля allauth
#
class SignupForm(forms.Form):

    error_css_class = 'error'
    username = forms.CharField(label = u"Имя пользователя",
                               max_length = 30,
                               min_length = 3,
                               widget = forms.TextInput(
                                   attrs = { 'placeholder': u"Имя пользователя",
                                             'autofocus': 'autofocus' }))
    email = forms.EmailField(widget = forms.TextInput(
                            attrs = { 'type': 'email',
                                        'placeholder': u'E-mail адрес' }))
    #password1 = SetPasswordField(label = u"Пароль")
    #password2 = PasswordField(label = u"Пароль (еще раз)")

    invite_code = forms.CharField(max_length = 20, label = u'Код приглашения',
                                  widget = forms.TextInput(
                                      attrs = { 'placeholder':
                                                    u'Код приглашения'}))
    #password2 = None

    def clean_invite_code(self):
        code = self.cleaned_data["invite_code"]
        #   Подключаем если нужно зарегистрировать людей без приглашения
        #if code:
        try:
            inv_db = Invitations.objects.get(code=code)
            if inv_db.invited:
               raise forms.ValidationError(u'Введенный код приглашения уже был ранее использован. Пожалуйста введите новый.')
        except Invitations.DoesNotExist:
            raise forms.ValidationError(u'Введенный код приглашения неверен.')
        return code


    def signup( self, request, user ):
        user.invite_code = self.cleaned_data['invite_code']
        inv_db = Invitations.objects.get(code=user.invite_code)
        #inv_db.user =
        print(user.invite_code)

        user.save()
'''
