# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.db import models
from facts.models import Facts
from accounts.models import CustomUser

# --------------------------------------------------------------------
#
# Описываем поля базы данных приглашений для пользователей
#
#--------------------------------------------------------------------
class Invitations(models.Model):
	class Meta():
		db_table = "dobro_invitations"  # Название таблицы
		verbose_name = 'Приглашение'
		verbose_name_plural = "Приглашения"

	code = models.CharField(verbose_name = "Код приглашения", max_length = 20, unique = True)
	email = models.EmailField(verbose_name = "E-mail адресата",
	                          blank = False, unique = True,
	                          validators = [validate_email],
	                          help_text = 'Введите пожалуйста email адресата',
	                          )
	accost = models.CharField( verbose_name = "ФИО адресата",
	                           blank = False, max_length = 50,
	                           help_text = 'Введите пожалуйста ФИО адресата',)
	user = models.ForeignKey(CustomUser, verbose_name = "Приглашающий")
	date_create = models.DateTimeField(verbose_name = "Дата создания", auto_now_add = True)
	invited = models.IntegerField(default=0, verbose_name='Приглашенный', blank =True, null=True)

	def __unicode__( self ):
		return u'{code}'.format(code=self.code)
