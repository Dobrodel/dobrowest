# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserChangeForm
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):

    form = CustomUserChangeForm
    list_display = (
        'username', 'email', 'is_superuser', 'karma', 'is_public', 'is_active', 'last_login', 'date_joined', )
    list_filter = ('is_superuser', 'karma', 'is_public',)
    fieldsets = (
        ('Основная информация', { 'fields': ('email', 'username', 'password') }),
        ('Персональная информация', { 'fields': ('date_of_birth', 'first_name', 'last_name', 'foto', 'karma',) }),
        ('Допуски', { 'fields': ('is_superuser', 'is_public',) }),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2') }
         ),)

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
