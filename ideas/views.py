# -*- coding: utf-8 -*-
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.models import CustomUser
from dobrowest.utils import UserPassesTestMixin
from facts.models import Facts
from ideas.forms import IdeasForm
from ideas.models import Ideas


TEMPLATE_IDEAS = 'dobroboad.html'


def get_rollback_url( request ):
    return request.META['HTTP_REFERER']


# ------------------------------------------------------------------
#
#   Отображает опубликованные добрые идеи
#
#------------------------------------------------------------------
class Dobroboad(UserPassesTestMixin, ListView, ):
    model = Ideas
    template_name = TEMPLATE_IDEAS
    paginate_by = 2
    queryset = Ideas.objects.filter(published = True).order_by('type')

show_dashboad = Dobroboad.as_view()

# ------------------------------------------------------------------
#
# Обрабатывает создание новых идей
#
# ------------------------------------------------------------------
class IdeasCreate(UserPassesTestMixin, CreateView):
    model = Ideas
    form_class = IdeasForm
    http_method_names = ['post']
    template_name = 'idea_to_create.html'
    decorators = ['login_required']
    #succes_url = '/success/'

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
        return redirect(get_rollback_url(self.request))
        # return redirect(reverse('facts:detail', args = [id]))


icreate = IdeasCreate.as_view()


class IdeaEdit(UserPassesTestMixin, UpdateView):
    model = Ideas
    form_class = IdeasForm
    template_name = 'idea_to_edit.html'
    decorators = ['login_required', ]

    # def dispatch(self, request, *args, **kwargs):
    #        self.get_context_data(kwargs)
    #        return super(IdeaEdit,self).dispatch(request)


    def get_context_data( self, **kwargs ):
        ret = super(IdeaEdit, self).get_context_data(**kwargs)
        ret['idea_id'] = self.kwargs['pk']
        url = get_rollback_url(self.request)
        #self.request.session['urlback'] = "/".join(url.split('/')[-4:])
        self.request.session['urlback'] = url
        return ret

    def get_success_url( self ):
        ret = self.request.session['urlback']

        return ret
        #decorators = 'login_required'

        #def get_initial( self ):
        #    # GET method is allowed, so we need to have some antispam protection
        #    article = self.object.fact
        #    referer = urlparse(self.request.META.get('HTTP_REFERER', ''))
        #    if article.id not in referer.path:  # /slug/
        #        raise PermissionDenied()
        #    return self.initial

        #def form_invalid(self, form):
        #    return super(IdeaEdit, self).form_invalid(form)


iedit = IdeaEdit.as_view()


def Iidelete( request, pk ):
    '''
        Удаяем переданную в pk запись
    '''
    resp = redirect(request.META['HTTP_REFERER'])
    try:
        ideas = Ideas.objects.get(id = pk)
        if ideas.author.username == auth.get_user(request).username:
            ideas.delete()
        return resp
    except ObjectDoesNotExist:
        raise Http404


def dialog_yes_no( request, answer ):
    pass

class IdeaDelete(UserPassesTestMixin, DeleteView):
    model = Ideas
    form_class = IdeasForm
    template_name = 'idea_to_delete.html'
    decorators = ['login_required']

    def get_context_data( self, **kwargs ):
        ret = super(IdeaDelete, self).get_context_data(**kwargs)
        url = get_rollback_url(self.request)
        self.request.session['urlback'] = "/".join([x for x in url.split('/') if not '?' in x])
        return ret

    def get_success_url( self ):
        ret = self.request.session['urlback']
        return ret


idelete = IdeaDelete.as_view()
# ------------------------------------------------------------------
#
# Обрабатывает голосование за идею по трем принципам
#
# ------------------------------------------------------------------
def ivote( request, pk, like_id ):
    resp = redirect(request.META['HTTP_REFERER'])  # get_url_from_session(request))
    like_id = int(like_id)
    try:
        # if not id_idea in request.COOKIES:
        ideas = Ideas.objects.get(id = pk)
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


# ------------------------------------------------------------------
#
# Обрабатывает публикацию новых идей
#
# ------------------------------------------------------------------
def ipublic( request, pk ):
    resp = redirect(request.META['HTTP_REFERER'])  # get_url_from_session(request))
    try:
        ideas = Ideas.objects.get(id = pk)
        ideas.published = False if ideas.published else True
        ideas.save()
        return resp
    except ObjectDoesNotExist:
        raise Http404
