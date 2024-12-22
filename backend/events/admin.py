from django.contrib import admin
from .models import Event, Rating, RSVP   
from .forms import EventAdminForm

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm #overrding the default form
    list_display = ('title', 'date', 'location', 'category', 'user') # fields to be displayed in the admin panel
    list_filter = ('category', 'date', 'user') # adds filtering options in the admin sidebar to help narrow down records by these fields.
    search_fields = ('title', 'description', 'location') # adds a search bar to the admin panel to search for records by these fields.

class RatingAdmin(admin.ModelAdmin):
    # list_display specifies which fields will appear as columns in the list view for ratings.
    list_display = ('event', 'user', 'score', 'created_at')

    # list_filter adds filtering options in the admin sidebar, allowing you to filter ratings by score and creation date.
    list_filter = ('score', 'created_at')

    # search_fields enables a search bar to search by related event title and user username.
    # Use double underscores (`__`) to reference related model fields (e.g., event__title).
    search_fields = ('event__title', 'user__username')

class RSVPAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'status', 'updated_at')
    list_filter = ('status', 'updated_at')
    search_fields = ('event__title', 'user__username')

admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Rating, RatingAdmin)

