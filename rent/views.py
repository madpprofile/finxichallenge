from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RegisterForm

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()			
			return render(request, 'rent/detail.html', {'instance': instance})
	else:
		form = RegisterForm()

	return render(request, 'rent/register.html', {'form': form})
	
def success(request):
	return render(request, 'rent/success.html')
