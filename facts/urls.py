# -*- coding: utf-8 -*-
from django.conf.urls import url

urlpatterns = [
    #url(r'^facts/', 'ideas.views.show_facts'),
    #url(r'^get/(?P<facts_id>\d+)/(?P<ideas_page>\d+)/$', 'facts.views.show_ideas'),
    # url(r'^addlike/(?P<id_idea>\d+)/(?P<like_id>\d+)/$','ideas.views.addlike', name = 'addlike'),
    #url(r'^addidea/(?P<id_fact>\d+)/(?P<ideas_page>\d+)/$','facts.views.create_idea'),

    #url(r'^page/(?P<page>\d+)/$', 'facts.views.show_list'),  # newone
    url(r'^id/(?P<pk>\d+)/$', 'facts.views.show_detail', name='detail'),  # newone
    #url(r'^fact/(?P<pk>\d+)/(?P<page>\d+)/$', 'facts.views.show_detail','detail-by-page'),  # newone
    url(r'^$', 'facts.views.show_list'),                     # newone

]
