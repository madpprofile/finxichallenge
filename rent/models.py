from django.db import models
import geocoder

def upload_location(instance, filename):
	filebase, extension = filename.rsplit(".", 1)
	return "%s/%s.%s" %(instance.id, instance.id, extension)

class Building(models.Model):
	number = models.IntegerField()
	apartment = models.IntegerField(blank=True, null=True)
	street = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	latitude = models.FloatField()
	longitude = models.FloatField()
	picture = models.ImageField(upload_to=upload_location)
	
	
	def address(self):
		return '%s %s, %s - %s' %(self.number, self.street, self.state, self.country)
	
	def admin_thumbnail(self):
		return u'<img src="%s" style="width: 150px; height: 150px"/>' % (self.picture.url)
	admin_thumbnail.short_description = 'Thumbnail'
	admin_thumbnail.allow_tags = True
	
	def __str__(self):
		return self.address()
