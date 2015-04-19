# -*- coding: utf-8 -*-
import smtplib
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from dobrowest import settings


__author__ = 'adam'
#
# -----------------------------------------------------
#   
#   Проект: dobrowest
#   Имя файла: views.py
#   Дата создания: 13.04.15 
#   Время создания: 11:41
#   Автор проекта: adam
#
#-----------------------------------------------------
#
from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.template.response import TemplateResponse
from django.core.context_processors import csrf
# -----------------------------------------------------
#
#   Импортируй свои модели
#
# -----------------------------------------------------
from invitations.models import Invitations
from forms import InvitationForm
from dobrowest.functions import generate_password, get_url_from_session, save_url_to_session
from accounts.models import CustomUser

KEY_INVITATION = 'invitation_key'
#
#-----------------------------------------------------
#  
#   Функция описывает ....
#
#-----------------------------------------------------  
def show( request ):
	args = { 'username': auth.get_user(request).username }
	#   Опиши переменные которые требуются в main.html
	
	#   Опиши переменные в шаблонах приложения
	invform = InvitationForm
	args.update(csrf(request))
	args['form'] = InvitationForm
	save_url_to_session(request)

	#   Пердай данные фкпы в подготовленный заранее шаблон
	return render_to_response('invite.html', args)


def validateEmail( email ):
	from django.core.validators import validate_email
	from django.core.exceptions import ValidationError


	try:
		validate_email(email)
		return True
	except ValidationError:
		return False

def make( request ):
	#assert False,  request.POST
	args={'username': auth.get_user(request).username}
	args.update(csrf(request))
	if request.POST:
		show_form = InvitationForm(request.POST)
		if show_form.is_valid():
			invite_form = show_form.save(commit = False)
			#assert False,  invite_form
			code = generate_password(9)
			fio = ' '.join([word.capitalize() for word in invite_form.accost.split(' ')])
			invite_form.accost = fio
			invite_form.code = code
			invite_form.user = CustomUser.objects.get(pk=auth.get_user(request).id)
			invite_form.save()
			email_body = render_to_string('email.html',{'data': invite_form})
			#email_body = strip_tags(email_body)
			try:
				send_mail(subject=invite_form.accost,
			          message=email_body,
			          from_email=settings.EMAIL_HOST_USER,
			          recipient_list=[invite_form.email],
			          fail_silently = False)
			except smtplib.SMTPException:
				return HttpResponse(u'Проблемы с отправкой по протоколу SMTP.')
			response = redirect('/invitations/thanks/')
			response.set_cookie(key = KEY_INVITATION, value= show_form.instance.id, )
			return response
	else:
		show_form = InvitationForm
	args['form'] = show_form
	return  render_to_response('invite.html',args)

def thanks( request):
	if KEY_INVITATION in request.COOKIES:
		args={}
		inv_id = request.COOKIES.get(KEY_INVITATION)
		inv_data = Invitations.objects.get(pk = int(inv_id))
		args['username'] = auth.get_user(request).username
		args['data'] = inv_data
		return render_to_response('thanks.html', args)
	else:
		return redirect('/')
