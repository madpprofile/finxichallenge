from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import geocoder
from .forms import RegisterForm
from .models import Building, dist

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			print(instance.address)
			g = geocoder.google(instance.address)
			instance.latitude, instance.longitude = g.latlng
			print(instance.latitude)
			print(instance.longitude)
			instance.save()			
			return render(request, 'rent/detail.html', {'object': instance})
	else:
		form = RegisterForm()

	return render(request, 'rent/register.html', {'form': form})

def search(request):
	if not request.GET.get('qparam'):
		return redirect('/')
	else:
		param = request.GET.get('qparam')
	q = list(Building.objects.all())
	q = [item for item in q if param in item.address()]
	if not q:
		return render(request, 'rent/search.html', {'option' : 0} )
	elif len(q) == 1:
		i = q[0]
		q = Building.objects.filter(city=i.city, state=i.state, country=i.country)
		q = sorted(q, key=lambda place: dist(place, i))
		for i in q:
			print(dist(i, q[0]))
		return render(request, 'rent/search.html', {'list' : q, 'option' : 1})
	else:
		return render(request, 'rent/search.html', {'list' : q, 'option' : 2})