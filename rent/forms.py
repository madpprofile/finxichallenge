from django import forms
from . import models

class RegisterForm(forms.ModelForm):
	class Meta:
		model = models.Building
		fields = ['number', 'apartment', 'street', 'city', 'state', 'country', 'picture']
'''
class SearchForm(forms.Form):
	qparam = forms.CharField(label='Search', max_length=100)
'''