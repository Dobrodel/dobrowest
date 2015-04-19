# -*- coding: utf-8 -*-
import invitations


__author__ = 'adam'
#
# -----------------------------------------------------
#   
#   Проект: dobrowest
#   Имя файла: urls.py
#   Дата создания: 13.04.15 
#   Время создания: 11:08
#   Автор проекта: adam
#
#-----------------------------------------------------
#
from django.conf.urls import url
#
#-----------------------------------------------------
#
#   Описываем реакцию на ввод ссылок 
#   в приложении urls
#
#-----------------------------------------------------
#
urlpatterns = [
    url(r'^send/$', 'invitations.views.make'),
    url(r'^thanks/$', 'invitations.views.thanks'),
    url(r'^', 'invitations.views.show'),

            ]
