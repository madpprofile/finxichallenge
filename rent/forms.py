from django import forms
from . import models

class RegisterForm(forms.ModelForm):
	class Meta:
		model = models.Building
		fields = ['number', 'apartment', 'street', 'city', 'state', 'country', 'picture']