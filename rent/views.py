from django.shortcuts import render
from django.http import HttpResponseRedirect
import geocoder
from .forms import RegisterForm

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			print(instance.address)
			g = geocoder.google(instance.address())
			instance.latitude, instance.longitude = g.latlng
			print(instance.latitude)
			print(instance.longitude)
			instance.save()			
			return render(request, 'rent/detail.html', {'object': instance})
	else:
		form = RegisterForm()

	return render(request, 'rent/register.html', {'form': form})
	
def success(request):
	return render(request, 'rent/success.html')
