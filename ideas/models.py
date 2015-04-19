# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models
from dobrowest.functions import get_path_to_image
from facts.models import Facts
from accounts.models import CustomUser

#--------------------------------------------------------------------
#
# Описываем поля базы данных типов тегов добавляемых одобрений
#
#--------------------------------------------------------------------
class Tags(models.Model):
    class Meta():
        db_table = "dobro_tags"  # Название таблицы
        verbose_name = verbose_name_plural = "Метки идей"

    name = models.CharField(verbose_name="Метка", max_length=20, unique=True)
    desc = models.TextField(verbose_name="Описание", blank=True, default='')

    def __unicode__( self ):
        return u'{display_name}'.format(display_name = self.name)

#--------------------------------------------------------------------
#
# Описываем поля базы данных категорий добавляемых новостей
#
#--------------------------------------------------------------------
class Category(models.Model):
    class Meta():
        db_table = "dobro_category"  # Название таблицы
        verbose_name = verbose_name_plural = "Разделы публикаций"

    name = models.CharField(verbose_name="Категория", max_length=20, unique=True)
    desc = models.TextField(verbose_name="Описание", blank=True, default='')

    def __unicode__( self ):
        return u'{display_name}'.format(display_name = self.name)

#--------------------------------------------------------------------
#
# Описываем поля базы данных одобренных новостей
#
#--------------------------------------------------------------------
class Ideas(models.Model):
    class Meta():
        db_table = "dobro_ideas"  # Название таблицы
        verbose_name = verbose_name_plural = "Добрые идеи"

    TYPE_OF_NEWS = ((1, 'Тема'),
                    (2, 'Статья'),
                    (3, 'Комментарий'))
    type = models.IntegerField(choices=TYPE_OF_NEWS, default=1, verbose_name = "Тип идеи", help_text = 'Выбирите тип Вашей идеи')

    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add = True )
    date_update = models.DateTimeField(verbose_name = "Дата обновления", auto_now = True)
    text = models.TextField( verbose_name = "Ваша идея", blank = False, help_text = 'Введите пожалуйста Вашу идею по поводу статьи, смысл которой отвечал бы трем основным принципам проекта: Добро, Радость, Развитие')
    foto = models.ImageField(upload_to=get_path_to_image, verbose_name="Фото", blank=True)
    published = models.BooleanField(verbose_name = "Опубликована", blank = True, default=False)

    dobro_like = models.IntegerField(verbose_name="Доброта", default=0, help_text = 'Здесь есть добро!')
    radost_like = models.IntegerField(verbose_name="Радость", default=0, help_text = 'Здесь есть радость!')
    razvitie_like = models.IntegerField(verbose_name="Развитие", default=0, help_text = 'Здесь есть развитие!')

    # Указатель на категорию новостей
    # как "много в DobroNews к одному в Category"
    category = models.ForeignKey(Category, verbose_name="Категория новостей", blank=False)

    # Указатель на автора статьи
    # как "много в DobroNews к одному в Facts"
    author = models.ForeignKey(CustomUser, verbose_name="Автор статьи", blank=False)

    # Указатель на принадлежность к старой статье
    # как "много в DobroNews к одному в Facts"
    fact = models.ForeignKey(Facts, verbose_name="Источник статьи", blank=False)

    # Указатель тегов/категорий новостей,
    # как "много в DobroNews к много в Tags"
    tag = models.ManyToManyField(Tags, verbose_name="Метки статьи", blank=True, default=None)

    def get_tags_list(self):
        return u", ".join([tag.name for tag in self.tag.all()])

    def get_author_name(self):
        return CustomUser.objects.get(id = self.author_id).username

    def get_idea_type(self):
        return self.get_type_display()


    def __unicode__( self ):
        return u'{display_name}'.format(display_name=self.text)

    def clean_text(self):
        if self.text.isdigit():
            raise ValidationError('Пожалуйста, введите текст.')

    def clean_category(self):
        if not self.category:
            raise ValidationError('Подскажите пожалуйста, к какой категории относится Ваша идея?')

#--------------------------------------------------------------------
#
#   Описываем поля базы данных для регистрации голосов пользователей
#
#--------------------------------------------------------------------
class UserVoices(models.Model):

    class Meta():
        db_table = "dobro_uservoices"  # Название таблицы
        verbose_name = verbose_name_plural = "Голосование"

    user = models.ForeignKey(CustomUser, verbose_name = "Индификатор пользователя", db_index = True, blank = False)
    ideas = models.ForeignKey(Ideas, verbose_name = "Индификатор идеи", db_index = True, blank = False)
    dobro = models.BooleanField(verbose_name="Принцип добра", default=0)
    razvitie = models.BooleanField(verbose_name = "Принцип развития", default = 0)
    radost = models.BooleanField(verbose_name = "Принцип радости", default = 0)

