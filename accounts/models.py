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
class CustomUser(User):

    class Meta():
        db_table = "dobro_accounts"
        verbose_name = verbose_name_plural = "Профили пользователей сайта"

    karma = models.IntegerField(verbose_name = "Карма", default = 0)
    is_public = models.BooleanField(verbose_name = "Публикатор", default = False)
    foto = models.ImageField(verbose_name = "Фото", upload_to = 'images/%Y/%m/%d', blank = True, null = True)
    date_of_birth = models.DateTimeField(verbose_name = "Дата рождения", blank = True, null = True )

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



