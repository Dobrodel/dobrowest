# -*- coding: utf-8 -*-
__author__ = 'adam'
#
# -----------------------------------------------------
#   
#   Проект: dobrowest
#   Имя файла: forms.py
#   Дата создания: 16.04.15 
#   Время создания: 19:40
#   Автор проекта: adam
#
#-----------------------------------------------------
#
from django.forms import ModelForm, widgets
from django import forms
from django.utils.safestring import mark_safe

from ideas.models import Ideas



#
#
# Виджет для отображения существующего фото при
# редактировании записей в режиме предостмотра
#
class FotoWidget(forms.FileInput):
	def __init__( self, attrs = { } ):
		super(FotoWidget, self).__init__(attrs)

	def render( self, name, value, attrs = None ):
		output = []
		if value and hasattr(value, "url"):
			output.append(('<a target="_blank" href="%s">'
			               '<img src="%s" style="height: 100px;" /></a> '
			               % (value.url, value.url)))
		output.append(super(FotoWidget, self).render(name, value, attrs))
		return mark_safe(u''.join(output))

#-----------------------------------------------------
#
#   Класс описывает форму ввода ...
#
#-----------------------------------------------------
#
class IdeasForm(ModelForm):

	class Meta():
		model = Ideas
		fields = ['text', 'type','category', 'fact', 'foto', 'tag']
		widgets = {
		'fact': widgets.HiddenInput,
		'foto': FotoWidget,  # 'text': PagedownWidget,
		'text': widgets.Textarea(attrs = { 'placeholder': 'Добавьте добрую идею!' })
		}

#	newtag = forms.CharField( widget=widgets.TextInput(attrs = { 'placeholder': 'Добавьте или найдите существующую метку!' }))
