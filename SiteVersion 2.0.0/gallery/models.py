from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GalleryModel(models.Model):
	image = models.ImageField(upload_to = 'image_gallery', blank = False)
	title = models.CharField(max_length = 30)

	class Meta:
		ordering = ('title',)
		verbose_name = 'Image'
		verbose_name_plural = 'Images'
        
	def __str__(self):
		return self.title