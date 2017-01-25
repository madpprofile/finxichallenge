from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from .models import Building

urlpatterns = [
	url(r'^register/$', views.register, name="register"),
	url(r'^buildings/(?P<pk>\d+)$', DetailView.as_view(
                            model = Building,
                            template_name="rent/detail.html")),
	url(r'^search/', views.search),
	url(r'^$', ListView.as_view(
							queryset=Building.objects.all(),
							template_name="rent/list.html"))
]
