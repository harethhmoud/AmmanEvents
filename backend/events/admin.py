from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_time', 'location', 'created_by')
    search_fields = ('title', 'description', 'location')
    list_filter = ('category', 'is_paid')
    
    

admin.site.register(Event, EventAdmin)

