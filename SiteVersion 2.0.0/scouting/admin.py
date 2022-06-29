from __future__ import unicode_literals

from django.contrib import admin
from .models import (ScoutData,
                    MatchData,
                    EventModel)

# Register your models here.

class ScoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'script']
    prepopulated_fields = {'script': ('name',)}

admin.site.register(ScoutData, ScoutAdmin)

admin.site.register(MatchData)

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(EventModel, EventAdmin)