from django.contrib import admin
from .models import Event

# Register your models here.

# Tells Django how to display the Event model in the admin interface
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_time', 'location', 'organizer')
    search_fields = ('title', 'description', 'location', 'organizer__username')
    list_filter = ('category',)
    
    

admin.site.register(Event, EventAdmin)

