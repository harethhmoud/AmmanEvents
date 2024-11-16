from django.contrib import admin
from .models import Event, Rating   
from .forms import EventAdminForm

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Rating)

