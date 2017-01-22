from django.db import models

def upload_location(instance, filename):
	filebase, extension = filename.rsplit(".", 1)
	return "%s/%s.%s" %(instance.id, instance.id, extension)

class Building(models.Model):
	address = models.CharField(max_length=200)
	picture = models.ImageField(upload_to=upload_location)
	
	def __str__(self):
		return self.address
