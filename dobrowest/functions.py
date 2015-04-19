# -*- coding: utf-8 -*-
__author__ = 'adam'
#
# -----------------------------------------------------
#   
#   Проект: dobrowest
#   Имя файла: functions.py
#   Дата создания: 13.04.15 
#   Время создания: 12:19
#   Автор проекта: adam
#
#-----------------------------------------------------
#
import string
import os
from random import choice
import hashlib

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


CURRENT_URL_TAG = 'urlTag'


def get_path_to_image( instance, filename ):
	ret = None
	if filename:
		me, ext = os.path.splitext(filename)
		md5hash = hashlib.md5(filename).hexdigest()
		hashname = "{name}{extension}".format(name = md5hash, extension = ext)
		prefix = instance.__class__.__name__.lower()
		ret = os.path.join(prefix, hashname[:2], hashname[2:4], hashname)
	return ret

# -----------------------------------------------------
#
# Функция генерирует пароль заданной длины
#
#-----------------------------------------------------
def generate_password( min_len = 8 ):
	return ''.join([choice(string.letters + string.digits) for i in range(min_len)])


# -----------------------------------------------------
#
# Функция сохраняет в сессии текущий путь с которого уходим
#
# -----------------------------------------------------
def save_url_to_session( request ):
	# Записываем текущий путь до страницы
	global CURRENT_URL_TAG
	request.session[CURRENT_URL_TAG] = request.get_full_path()


# -----------------------------------------------------
#
# Функция восстанавливает из сессии предыдущий путь
#
# -----------------------------------------------------
def get_url_from_session( request):
	global CURRENT_URL_TAG
	request.session[CURRENT_URL_TAG]


# -----------------------------------------------------
#
# Функция восстанавливает из сессии предыдущий путь
#
# -----------------------------------------------------

def send_template_by_email( request ):
	subject = request.POST.get('subject', '')
	message = request.POST.get('message', '')
	from_email = request.POST.get('from_email', '')

	if subject and message and from_email:
		try:
			send_mail(subject, message, from_email, ['admin@example.com'])
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return HttpResponseRedirect('/contact/thanks/')
	else:
		# In reality we'd use a form class
		# to get proper validation errors.
		return HttpResponse('Make sure all fields are entered and valid.')
