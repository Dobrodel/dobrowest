# -*- coding: utf-8 -*-
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
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
        return redirect(reverse('facts:detail', args = [id]))

create_idea = IdeasCreate.as_view()


def addlike( request, id_idea, like_id ):
    resp = redirect(request.META['HTTP_REFERER'])  # get_url_from_session(request))
    like_id = int(like_id)
    try:
        # if not id_idea in request.COOKIES:
        ideas = Ideas.objects.get(id = id_idea)
        if like_id == 1:
            ideas.dobro_like += 1
        elif like_id == 2:
            ideas.radost_like += 1
        elif like_id == 3:
            ideas.razvitie_like += 1

        ideas.save()
        #resp.set_cookie(id_blog, "test")
        return resp  #redirect('/facts/get/1/1/')
        #else:
        #    return redirect('/')
    except ObjectDoesNotExist:
        raise Http404
