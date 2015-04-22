# -*- coding: utf-8 -*-

from django.conf.urls import url


urlpatterns = [
	#url(r'^ideas/all/$', 'ideas.views.blogShowAll'),
	#url(r'^ideas/get/(?P<id_blog>\d+)/(?P<page_number>\d+)/$', 'ideas.views.blog'),
	#url(r'^addlike/(?P<id_blog>\d+)/(?P<id_page>\d+)/$', 'ideas.views.addlike', name='addlike'),
	#url(r'^', 'ideas.views.addlike'),
	#url(r"^add/$", IdeasCreate.as_view(), name='add'),
	url(r"^create/$", 'ideas.views.icreate', name = 'create'),
	url(r'^vote/(?P<pk>\d+)/(?P<like_id>\d+)/$', 'ideas.views.ivote', name = 'vote'),
	url(r'^public/(?P<pk>\d+)/$', 'ideas.views.ipublic', name = 'public'),
	url(r'^edit/(?P<pk>\d+)/$', 'ideas.views.iedit', name = 'edit'),
	url(r'^delete/(?P<pk>\d+)/$', 'ideas.views.idelete', name = 'delete'),
	#url(r'^page/(?P<page>\d+)/$', 'ideas.views.show_list'),
    #url(r'^', 'ideas.views.show_dashboad'),

]
