from django.contrib import admin
from .models import Event, TicketTier

# Tells Django how to display the Event model in the admin interface
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_time', 'location', 'organizer')
    search_fields = ('title', 'description', 'location', 'organizer__username')
    list_filter = ('category',)

admin.site.register(Event, EventAdmin)

# Customize the TicketTier view so you can easily manage tiers
class TicketTierAdmin(admin.ModelAdmin):
    list_display = ('tier_name', 'price', 'event')
    search_fields = ('tier_name', 'event__title')
    list_filter = ('tier_name',)

admin.site.register(TicketTier, TicketTierAdmin)