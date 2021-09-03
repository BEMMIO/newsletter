from django.shortcuts import render,redirect

from . import forms
# Create your views here.
from .tasks import test_celery_func,send_email

def subscribe_for_newsletter(request,template='subscribe/index.html',*args,**kwargs):

	form 	=	forms.SubscribeForm()

	# testing celery
	test_celery_func.delay()

	if request.method == "POST":
		form = forms.SubscribeForm(data = request.POST)
		if form.is_valid():
			email = request.POST.get('email',None)

			# celery email 
			send_email.delay(email)
			return redirect('subscribe:subscribe-for-newsletter')
		else:
			pass

	ctx = {
	'form':form
	}
	return render(request,template,ctx)




def thank_you(request,template='subscribe/thank_you_for_subscribing.html',*args,**kwargs):

	return render(request,template,{})