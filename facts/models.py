# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# --------------------------------------------------------------------
#
# Описываем поля базы данных еще неодобренных новостей
#
#--------------------------------------------------------------------
class Facts(models.Model):
    class Meta():
        db_table = "dobro_facts"  # Название таблицы
        verbose_name = verbose_name_plural = "Голые факты"

    title = models.CharField(verbose_name="Заголовок", max_length=200)
    text = models.TextField(verbose_name="Содержание", blank=False)
    date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    source_url = models.URLField(verbose_name="Источник", default='/', blank=True)
    foto = models.ImageField(verbose_name="Фото", blank=True)


    def __unicode__( self ):
        return u'%s' % self.title
