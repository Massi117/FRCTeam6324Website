from __future__ import unicode_literals

from django.db import models

# These are models for site contents

class SponsorClassModel(models.Model):
    name = models.CharField(max_length = 200, db_index = True)
    shortcode = models.CharField(max_length = 200, db_index = True, unique = True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'class'
        verbose_name_plural = 'classes'
        
    def __str__(self):
        return self.name


class SponsorModel(models.Model):   
    
    category = models.ForeignKey(SponsorClassModel, related_name='sponsors')
    name = models.CharField(max_length =200, db_index = True)
    image = models.ImageField(upload_to='sponsor_image', blank=True)
    slug = models.CharField(max_length = 200, db_index = True, unique = True)

    description = models.TextField(blank = True)

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
    

    def __str__(self):
	return self.name

class MemberModel(models.Model):

    student = models.CharField(max_length =200, db_index = True)
    last = models.CharField(max_length =200, db_index = True, default="")

    class Meta:
        ordering = ['last', 'student']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.student


class StaffModel(models.Model):

    staff = models.CharField(max_length =200, db_index = True)
    last = models.CharField(max_length =200, db_index = True, default="")

    class Meta:
        ordering = ['last', 'staff']
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return self.staff

class Header(models.Model):

    title = models.CharField(max_length=100)
    button = models.CharField(max_length=20, blank = True)
    body = models.TextField(blank = True)
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title

    
class CommunityBlock(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField(blank = True)
    image = models.ImageField(upload_to='sponsor_image', blank=True)
    place = models.BooleanField()

    class Meta:
        verbose_name = 'Community Block'
        verbose_name_plural = 'Community Blocks'

    def __str__(self):
        return self.title

class HistoryBlock(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField(blank = True)
    image = models.ImageField(upload_to='sponsor_image', blank=True)
    place = models.BooleanField()

    class Meta:
        verbose_name = 'History Block'
        verbose_name_plural = 'History Blocks'

    def __str__(self):
        return self.title


class ContactModel(models.Model):

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name
