from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
class Celebrity(models.Model):
    name = models.CharField()

class Image(models.Model):
    celebrity = models.ForeignKey(Celebrity)
    image = models.ImageField()

class InlineImage(admin.TabularInline):
    model = Image


class CelebrityAdmin(admin.ModelAdmin):
    inlines = [InlineImage]'''

class Event(models.Model):
	heading=models.CharField(max_length=50)
	image=models.ImageField(upload_to='static/eventimages')

class Teacher(models.Model):
	Name=models.CharField(max_length=50)
	Image=models.ImageField()


