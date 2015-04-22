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
        verbose_name = verbose_name_plural = u"Голые факты"

    title = models.CharField(verbose_name = u"Заголовок", max_length = 200)
    text = models.TextField(verbose_name = u"Содержание", blank = False)
    date = models.DateTimeField(verbose_name = u"Дата создания", auto_now_add = True)
    source_url = models.URLField(verbose_name = u"Источник", default = '/', blank = True)
    # foto = CustomImageFields(verbose_name = u"Фото", blank = True, )

    foto = models.ImageField(verbose_name="Фото", blank=True)


    def __unicode__( self ):
        return u'%s' % self.title
