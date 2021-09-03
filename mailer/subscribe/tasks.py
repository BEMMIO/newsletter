# celery config imports
from celery.decorators import task
from celery import shared_task

# Email config imports
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError



@task
def send_email(email):

	domain = settings.SITE_DOMAIN
	url = 'https://{}/thank-you/'.format(domain)

	context = {
	'url':url,
	'domain': domain,
	'client_email': email
	}

	message = get_template(
			template_name = 'subscribe/mail.html'
	).render(context)

	subject = 'Thank You for Subscribing to My Website !'
	to_email = email

	from_email = settings.DEFAULT_FROM_EMAIL

	email = EmailMessage(
		subject,message,from_email,[to_email]
	)

	email.content_subtype = "html"

	try:
		email.send()
	except BadHeaderError as e:
		pass


# Just a Test
@shared_task(bind=True)
def test_celery_func(self):
	for i in range(30):
		print(i)
	return "CELERY IS WORKING PERFECTLY !"