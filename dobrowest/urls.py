# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
                url(r'^accounts/', include('allauth.urls')),
                url(r'^admin/', include(admin.site.urls)),
                url(r'^admin_tools/', include('admin_tools.urls')),
                url(r'^facts/', include('facts.urls', namespace = 'facts')),
                url(r'^ideas/', include('ideas.urls', namespace = 'ideas')),
                url(r'^invitations/', include('invitations.urls')),
                url(r'^media/(\w+)/(\d+)/(\d+)/$',''),
                url(r'^', include('facts.urls')),
            ]
