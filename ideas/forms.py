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
from django.forms import ModelForm
from ideas.models import Ideas
from django.forms import ModelForm, widgets
#from pagedown.widgets import PagedownWidget
from django import forms
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
		#'parent': widgets.HiddenInput,
		#'text': PagedownWidget,
		'text': widgets.TextInput(attrs = { 'placeholder':'Добавьте добрую идею!' })
		}

#	newtag = forms.CharField( widget=widgets.TextInput(attrs = { 'placeholder': 'Добавьте или найдите существующую метку!' }))
