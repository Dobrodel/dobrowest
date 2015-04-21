# -*- coding: utf-8 -*-
'''
	   Проект: dobrowest
	   Имя файла: forms.py
	   Дата создания: 16.04.15
	   Время создания: 19:40
	   Автор проекта: adam
'''
from django.forms import ModelForm, widgets

from ideas.models import Ideas
from dobrowest.utils import ImageWidget




#-----------------------------------------------------
#
#   Класс описывает форму ввода ...
#
#-----------------------------------------------------
#
class IdeasForm(ModelForm):
	'''
		Класс описывает форму ввода идей
	'''
	class Meta():
		model = Ideas
		fields = ['text', 'type','category', 'fact', 'foto', 'tag']
		widgets = {
		'fact': widgets.HiddenInput,
		'foto': ImageWidget,  # 'text': PagedownWidget,
		'text': widgets.Textarea(attrs = { 'placeholder': u'Добавьте добрую идею!' })
		}

#	newtag = forms.CharField( widget=widgets.TextInput(attrs = { 'placeholder': 'Добавьте или найдите существующую метку!' }))
