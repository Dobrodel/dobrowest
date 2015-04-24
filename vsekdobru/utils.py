# -*- coding: utf-8 -*-
'''
	Проект: vsekdobru
    Имя файла: utils.py
    Дата создания: 13.04.15
    Время создания: 12:19
    Автор проекта: adam

'''  #
import os
import hashlib
from os.path import splitext

from django.conf.global_settings import LOGIN_URL
from django.contrib import auth
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat


# ---------------------------------------------------------------------
from django_resized import ResizedImageField


class UserPassesTestMixin(object):
	'''
		Позволяет детям производить операции
		только авторизированным пользователям
	'''

	def user_passes_test( self, user ):
		return user.is_authenticated()

	def user_failed_test( self ):
		return redirect(LOGIN_URL)

	def dispatch( self, request, *args, **kwargs ):
		if not self.user_passes_test(request.user):
			return self.user_failed_test()
		return super(UserPassesTestMixin, self).dispatch(request, *args, **kwargs)

	def get_context_data( self, **kwargs ):
		ret = super(UserPassesTestMixin, self).get_context_data(**kwargs)
		ret['username'] = auth.get_user(self.request).username
		return ret


class ImageWidget(forms.FileInput):
	'''
		Виджет для отображения существующего фото при
	    редактировании записей в режиме предостмотра
	'''

	def __init__( self, attrs = { } ):
		super(ImageWidget, self).__init__(attrs)

	def render( self, name, value, attrs = None ):
		output = []
		if value and hasattr(value, "url"):
			output.append(('<a target="_blank" href="%s">'
			               '<img src="%s" style="height: 100px;" /></a> '
			               % (value.url, value.url)))
		output.append(super(ImageWidget, self).render(name, value, attrs))
		return mark_safe(u''.join(output))


class FileValidator(object):
	"""
		Класс позволяет проверить данные загружаемых файлов и установить ограничения
		по их размерам и рассширениям.
		Источник: https://gist.github.com/dokterbob/1183767

		Параметры иницилизации:
			allowed_extensions: список допустимых расширений
				например - ['txt', 'doc']
			min_size: минимально допустимый размер в байтах
				например - 1*1024 для 1 KB
			max_size: максимально допустимый размер в байтах
				например - 24*1024*1024 для 24 MB

		Пример использования:

			MyModel(models.Model):
				myfile = FileField(validators=[FileValidator(max_size=24*1024*1024)], ...)
	"""

	extension_message = u"Расширение файла '{extension} не допустимо. Вы можете загружать файлы следующих форматов: '{allowed_extensions}.'"
	min_size_message = u'Текущий размер файла ({size}) очень мал. Минималный размер файла ограничен {allowed_size}.'
	max_size_message = u'Текущий размер файла ({size}) слишком велик. Макимальный размер файла не может превышать {allowed_size}.'

	def __init__( self, *args, **kwargs ):
		self.allowed_extensions = kwargs.pop('allowed_extensions', None)
		self.allowed_mimetypes = kwargs.pop('allowed_mimetypes', None)
		self.min_size = kwargs.pop('min_size', 0)
		self.max_size = kwargs.pop('max_size', None)

	def __call__( self, value ):
		"""
		Проверяет при вызове размеры и рассширение файла.
		"""
		# Проверка рассширения
		ext = splitext(value.name)[1][1:].lower()
		if self.allowed_extensions and not ext in self.allowed_extensions:
			message = self.extension_message.format(
				extension = ext,
				allowed_extensions = ', '.join(self.allowed_extensions))
			raise ValidationError(message)

		# Проверка размеров файла
		filesize = value.file.size
		if self.max_size and filesize > self.max_size:
			message = self.max_size_message.format(
				size = filesizeformat(filesize),
				allowed_size = filesizeformat(self.max_size))
			raise ValidationError(message)

		if self.min_size and filesize < self.min_size:
			message = self.min_size_message.format(
				size = filesizeformat(filesize),
				allowed_size = filesizeformat(self.min_size))
			raise ValidationError(message)


class CustomImageFields(ResizedImageField):
	'''
	   Функция создает поле для изображения для построения модели
	   И использует следующие ограничения при его загрузке:
	   Минимальный размер файла -  15Kb
	   Допустимые расширения файлов - 'bmp','png','jpg','jpeg','gif'
	'''
	MIN_IMAGE_SIZE = 60 * 1024  # 15Kb
	MAX_IMAGE_WIDTH = 800
	MAX_IMAGE_HEITHT = 600
	IMAGE_EXTENSIONS = ['bmp', 'png', 'jpg', 'jpeg', 'gif', ]

	def __init__( self, verbose_name = u'Изображение', blank = True, **kwargs ):
		self.size = [self.MAX_IMAGE_WIDTH, self.MAX_IMAGE_HEITHT]
		self.crop = ['middle', 'center']
		self.upload_to = get_path_to_image
		self.blank = blank
		self.null = True
		self.validators = [FileValidator(
			allowed_extensions = self.IMAGE_EXTENSIONS,
			min_size = self.MIN_IMAGE_SIZE)]
		super(CustomImageFields, self).__init__(verbose_name = verbose_name, name = None, **kwargs)

	# img = models.FileField(upload_to = get_path_to_image,
	#                       verbose_name = verbose_name,
	##                       blank = blank, null = True,
	#                       validators = [FileValidator(
	#	                       allowed_extensions = IMAGE_EXTENSIONS,  # allowed_mimetypes=IMAGE_CONTEXT_TYPES,
	#	                       min_size = MIN_IMAGE_SIZE,
	#	                       max_size = MAX_IMAGE_SIZE)]
	#                       )


def get_path_to_image( instance, filename ):
	'''
	   Функция генерирует путь до папки хранения изображения
	   основываясь на сгенерированном хэш коде самого файла
	   Родительская папка состоит из двух первых символов кода
	   и дочерняя состоит из двух последующих цифр хэш кода
	'''
	ret = None
	if filename:
		me, ext = os.path.splitext(filename)
		md5hash = hashlib.md5(filename).hexdigest()
		hashname = "{name}{extension}".format(name = md5hash, extension = ext)
		prefix = instance.__class__.__name__.lower()
		ret = os.path.join(prefix, hashname[:2], hashname[2:4], hashname)
	return ret

