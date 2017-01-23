from django.contrib import admin
from .models import Building

class BuildingAdmin(admin.ModelAdmin):
	list_display = ('address', 'admin_thumbnail')
	search_fields = ['title']
	readonly_fields = ('address', 'picture', 'admin_thumbnail')
	
	def has_add_permission(self, request):
		return False

#	def has_change_permission(self, request):
#		return False

		
admin.site.register(Building, BuildingAdmin)