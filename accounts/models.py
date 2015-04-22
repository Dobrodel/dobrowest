# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save

#--------------------------------------------------------------------
#
#   Описываем поля базы данных своих пользователей
#   На основании системной таблицы пользователей Users
#
#--------------------------------------------------------------------
from dobrowest.utils import CustomImageFields


class CustomUser(User):

    class Meta():
        db_table = "dobro_accounts"
        verbose_name = verbose_name_plural = u"Профили пользователей сайта"

    karma = models.IntegerField(verbose_name = u"Карма", default = 0)
    is_public = models.BooleanField(verbose_name = u"Публикатор", default = False)
    # foto = models.ImageField(verbose_name = "Фото", upload_to = 'images/%Y/%m/%d', blank = True, null = True)
    foto = CustomImageFields(verbose_name = u"Фотография")
    date_of_birth = models.DateTimeField(verbose_name = u"Дата рождения", blank = True, null = True)

    objects = UserManager()


# --------------------------------------------------------------------
#
#   Функция синхронизации данных с системной базой пользователей User
#
#--------------------------------------------------------------------
def create_custom_user(sender, instance, created, **kwargs ):
    if created:
        values = {}
        for field in sender._meta.local_fields:
            values[field.attname] = getattr(instance, field.attname)
        user = CustomUser(**values)
        user.save()
    return

post_save.connect(create_custom_user, User)



