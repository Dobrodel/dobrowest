# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from ideas.views import IdeasCreate


urlpatterns = [
	#url(r'^ideas/all/$', 'ideas.views.blogShowAll'),
	#url(r'^ideas/get/(?P<id_blog>\d+)/(?P<page_number>\d+)/$', 'ideas.views.blog'),
	#url(r'^addlike/(?P<id_blog>\d+)/(?P<id_page>\d+)/$', 'ideas.views.addlike', name='addlike'),
	#url(r'^', 'ideas.views.addlike'),
	#url(r"^add/$", IdeasCreate.as_view(), name='add'),
	url(r"^add/$", 'ideas.views.create_idea', name = 'add'),
	url(r'^addlike/(?P<id_idea>\d+)/(?P<like_id>\d+)/$', 'ideas.views.addlike', name = 'addlike'),
	#url(r'^page/(?P<page>\d+)/$', 'ideas.views.show_list'),
    #url(r'^', 'ideas.views.show_dashboad'),

]
