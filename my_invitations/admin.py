from django.contrib import admin

# Register your models here.
from django.contrib import admin
from invitations.models import Invitations


# Register your models here.
class InviteAdmin(admin.ModelAdmin):
	fields = ['invited','email', 'code', 'user', 'accost', 'date_create']
	list_display = ('date_create','user', 'invited', 'accost', 'email', 'code',  )
	list_filter = ['user', 'date_create']

admin.site.register(Invitations, InviteAdmin)
