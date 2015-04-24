# -*- coding: utf-8 -*-
from django.contrib import auth
from django.views.generic import  ListView, DetailView

from ideas.forms import IdeasForm
from ideas.models import Ideas
from facts.models import Facts


TEMPLATE_FACTS = 'facts_list.html'
TEMPLATE_FACTS_DETAIL = 'facts_detail.html'
TEMPLATE_IDEAS = 'ideas_list.html'

#------------------------------------------------------------------
#
#   Отображает обычные факты/новсти
#
#------------------------------------------------------------------
class FactsView(ListView):
    template_name = TEMPLATE_FACTS
    model = Facts
    paginate_by = 2

    def get_context_data( self, **kwargs ):
        ret = super(FactsView, self).get_context_data(**kwargs)
        ret['username']= auth.get_user(self.request).username
        return ret

show_list = FactsView.as_view()


#------------------------------------------------------------------
#
#   Отображает выбранный факт и добрые идеи к ним
#
#------------------------------------------------------------------
class FactDetail(DetailView):
    model = Facts
    template_name = TEMPLATE_FACTS_DETAIL

    def get_context_data( self, **kwargs ):
        ret = super(FactDetail, self).get_context_data(**kwargs)
        # Используем для привязки идей в блоке обраотке идей
        self.request.session['fact_id']= self.object.pk
        ret['username'] = auth.get_user(self.request).username
        ret['form_create'] = IdeasForm(initial = { 'fact': self.object })
        ret['ideas_list'] = Ideas.objects.filter(fact_id=self.object.pk)
        return ret

show_detail = FactDetail.as_view()
