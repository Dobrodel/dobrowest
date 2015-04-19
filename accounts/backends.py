# -*- coding: utf-8 -*-
__author__ = 'adam'
#
# -----------------------------------------------------
#   
#   Проект: dobrowest
#   Имя файла: backends.py
#   Дата создания: 10.04.15 
#   Время создания: 8:19
#   Автор проекта: adam
#
#-----------------------------------------------------
#
from django.contrib.auth.backends import ModelBackend
from accounts.models import CustomUser

class CustomUserModelBackend(ModelBackend):

    user_class = CustomUser

    def authenticate(self, username = None, password = None, ** kwargs):
        try :
            user = self.user_class.objects.get(username=username)
            if user.check_password(password):
                return user
        except self.user_class.DoesNotExist:
            return None

    def get_user(self, user_id):
        try :
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None
