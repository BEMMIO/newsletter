from django.conf import settings

# from django.template.loader import get_template
# from django.core.mail import EmailMessage
# from django.core.mail import BadHeaderError

from django.db import models

# Create your models here.




class Subscribe(models.Model):

	email 			=		models.EmailField(max_length=150,blank=False,null=False)

	created_date 	= 		models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering 	=       (("-id"),)
		verbose_name = 		"Subscribe"
		verbose_name_plural = "Subscribe's"


	def __str__(self):
		return self.email


	def save(self,*args,**kwargs):
		super(self.__class__,self).save(*args,**kwargs)



	# @property
	# def send_mail(self):

	# 	domain = settings.SITE_DOMAIN


	# 	url = 'https://{}/thank-you/'.format(domain)

	# 	email = self.email

	# 	context = {
	# 	'url':url,
	# 	'domain': domain,
	# 	'client_email': email
	# 	}

	# 	message = get_template(
	# 		template_name = 'subscribe/mail.html'
	# 	).render(context)

	# 	subject = 'Thank You for Subscribing !'

	# 	to_email = email

	# 	from_email = settings.DEFAULT_FROM_EMAIL

	# 	email = EmailMessage(
	# 		subject,message,from_email,[to_email]
	# 	)

	# 	email.content_subtype = "html"

	# 	try:
	# 		email.send()
	# 	except BadHeaderError as e:
	# 		pass
