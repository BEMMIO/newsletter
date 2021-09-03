from django import forms

from . import models



class SubscribeForm(forms.ModelForm):

	email 		=  forms.EmailField(label="Email",
					required=True,
					widget=forms.EmailInput(
					attrs={'placeholder':'Enter your email to subscribe','autofocus':True}))

	class Meta:
		model 	=  models.Subscribe

		fields 	=  ("email",)


	def clean_email(self):
		return self.cleaned_data.get("email").lower()
