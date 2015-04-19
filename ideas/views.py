# -*- coding: utf-8 -*-
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from accounts.models import CustomUser
from facts.models import Facts
from ideas.forms import IdeasForm
from ideas.models import Ideas


TEMPLATE_IDEAS = 'dobroboad.html'


# ------------------------------------------------------------------
#
#   Отображает опубликованные добрые идеи
#
#------------------------------------------------------------------
class Dobroboad(ListView):
    model = Ideas
    template_name = TEMPLATE_IDEAS
    paginate_by = 2
    queryset = Ideas.objects.filter(published = True).order_by('type')

    def get_context_data( self, **kwargs ):
        ret = super(Dobroboad, self).get_context_data(**kwargs)
        ret['username'] = auth.get_user(self.request).username
        return ret

show_dashboad = Dobroboad.as_view()


class IdeasCreate(CreateView):
    model = Facts
    form_class = IdeasForm
    http_method_names = ['post']
    template_name = 'idea_create.html'
    #succes_url = '/success/'

    def get_context_data( self, **kwargs ):
        ret = super(IdeasCreate, self).get_context_data(**kwargs)
        ret.update({ "username": auth.get_user(self.request).username })
    #    fact_id = self.request.session['fact_id']
    #    ret['object'] = Facts.objects.get(id = fact_id)
    #    ret['form_create'] = IdeasForm(initial = { 'fact': fact_id })
    #    ret['ideas_list'] = Ideas.objects.filter(fact_id = fact_id)
        return ret

    def form_valid( self, form ):
        id = self.request.session['fact_id']
        author = auth.get_user(self.request).id
        try:
            idea = form.save(commit = False)
            img = self.request.FILES.get('foto')
            if img:
                idea.foto = img
            idea.fact = Facts.objects.get(id = id)
            idea.author = CustomUser.objects.get(pk = author)
            form.save()
        except Exception as e:
            return self.form_invalid(form)
        #return self.render_to_response(self.get_context_data(
                #success_message = 'Запись добавлена успешно!'))
        return redirect(reverse('facts:detail', args = [id]))

create_idea = IdeasCreate.as_view()
