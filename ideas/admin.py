# -*- coding: utf-8 -*-
from django.contrib import admin
from ideas.models import Tags, Category


# Register your models here.
class TagsAdmin(admin.ModelAdmin):
    fields = ['name', 'desc']
    list_filter = ['name']

class CategoriesAdmin(admin.ModelAdmin):
    fields = ['name', 'desc']
    list_filter = ['name']

admin.site.register(Tags, TagsAdmin)
admin.site.register(Category, CategoriesAdmin)
