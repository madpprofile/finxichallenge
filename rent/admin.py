from django.contrib import admin
from .models import Building

class BuildingAdmin(admin.ModelAdmin):
	list_display = ('address', 'admin_thumbnail')
	search_fields = ['number', 'apartment', 'street', 'city', 'state', 'country']
	readonly_fields = ('number', 'apartment', 'street', 'city', 'state', 'country', 'address', 'picture', 'admin_thumbnail', 'latitude', 'longitude')
	
	def has_add_permission(self, request):
		return False

#	def has_change_permission(self, request):
#		return False

		
admin.site.register(Building, BuildingAdmin)