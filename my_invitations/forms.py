# -*- coding: utf-8 -*-
import re


__author__ = 'adam'
#
# -----------------------------------------------------
#   
#   Проект: dobrowest
#   Имя файла: forms.py
#   Дата создания: 13.04.15 
#   Время создания: 9:47
#   Автор проекта: adam
#
#-----------------------------------------------------
#
from django.forms import ModelForm
from models import Invitations
from django import forms
#
#-----------------------------------------------------
#
#   Класс описывает форму ввода приглашений
#
#-----------------------------------------------------
#
class InvitationForm(ModelForm):
	error_css_class = 'error'
	class Meta:
		model = Invitations
		fields = ['email', 'accost']
		initial = { 'email': 'Введите email приглашаемого лица.',
                    'accost':'Введите ФИО приглашаемого лица.'}

	def clean_email( self ):
		email = self.cleaned_data['email']
		if (len(email) < 6) or (not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email)):
				raise forms.ValidationError(u'Введите правильный email!')
		return email

	def clean_accost(self):
		accost = self.cleaned_data['accost']
		if len(accost.split(' ')) > 3:
			raise forms.ValidationError(u'ФИО адресата НЕ должно содержать более 3 слов!')
		return accost


	def clean( self ):
		cleaned_data = super(InvitationForm, self).clean()
		email = cleaned_data.get("email")
		accost = cleaned_data.get("accost")
		if not email and not accost:
			raise forms.ValidationError(u"Заполните пожалуйста оба поля.")
		# Always return the full collection of cleaned data.
		return cleaned_data
