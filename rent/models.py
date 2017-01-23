from django.db import models

def upload_location(instance, filename):
	filebase, extension = filename.rsplit(".", 1)
	return "%s/%s.%s" %(instance.id, instance.id, extension)

class Building(models.Model):
	address = models.CharField(max_length=200)
	picture = models.ImageField(upload_to=upload_location)
	
	def admin_thumbnail(self):
		return u'<img src="%s" style="width: 150px; height: 150px"/>' % (self.picture.url)
	admin_thumbnail.short_description = 'Thumbnail'
	admin_thumbnail.allow_tags = True
	
	def __str__(self):
		return self.address
