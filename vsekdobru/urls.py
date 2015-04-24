# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from vsekdobru import settings


urlpatterns = [
                url(r'^accounts/', include('allauth.urls')),
                url(r'^admin/', include(admin.site.urls)),
                url(r'^admin_tools/', include('admin_tools.urls')),
                url(r'^facts/', include('facts.urls', namespace = 'facts')),
                url(r'^ideas/', include('ideas.urls', namespace = 'ideas')),
                url(r'^invitations/', include('invitations.urls')),
                url(r'^filldb/', 'vsekdobru.test.fillDB', name = 'test'),
                url(r'^', include('facts.urls')),
            ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
# patterns('',
# (r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 'django.views.static.serve',
#                   { 'document_root': settings.STATIC_ROOT }),
#          (r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve',
#           { 'document_root': settings.MEDIA_ROOT }),
#                               )
