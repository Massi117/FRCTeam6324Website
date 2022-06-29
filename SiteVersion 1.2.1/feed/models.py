from __future__ import unicode_literals
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='profile_image', blank=True, default='static img/default_profile.jpg')
    
    def __str__(self):
        return self.user.username
    
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
    
post_save.connect(create_profile, sender=User)

class Post(models.Model):
    title = models.CharField(max_length=100, blank = True)
    post = models.TextField(blank = True)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title