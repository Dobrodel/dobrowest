# -*- coding: utf-8 -*-

from django.contrib import admin
from facts.models import Facts
from ideas.models import Ideas

#
#   Описание видимых полей таблицы Ideas в панеле администратора
#   которые могут быть редактируемы вместе с таблицей Facts.
#
class GoodNewsInline(admin.StackedInline):
    model = Ideas
    fields = ['text', 'foto',
              'fact', 'type',
              'user','category',]
    list_display = ('text', 'get_tags_list','type','user','category',)
    extra = 4

#
#   Описание полей таблица Facts, которые
#   могут быть видимы и отфильтрованы по обозначенным полям
#   и совместно будет выводится c зависимой таблицей Ideas
#
class FactsAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'source_url', 'foto']
    inlines = [GoodNewsInline]
    list_display = ('date','title',)
    list_filter = ['date', 'source_url']

admin.site.register(Facts, FactsAdmin)
