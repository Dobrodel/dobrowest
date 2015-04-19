from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',

    #url(r'^send-invite/$', views.SendInvite(),#.as_view(),
    #    name='send-invite'),
    url(r'^send-invite/$', 'invitations.views.send_invitation', name = 'send-invitation'),
    #url(r'^send-invite/$', 'invitations.views.send_invitation', name = 'send-invitation'),
    #url(r'^thanks/$', 'invitations.views.show_thanks', name = 'send-thanks'),
    url(r'^accept-invitation/(?P<key>\w+)/$', 'invitations.views.accept_invitation', name='accept-invitation'),
    
)
