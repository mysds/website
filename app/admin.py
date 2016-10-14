from django.contrib import admin

# Register your models here.

from .models import Event,Teacher

admin.site.register(Event)


admin.site.register(Teacher)
