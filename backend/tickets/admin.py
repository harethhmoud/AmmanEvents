from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'ticket_tier', 'buyer', 'quantity', 'purchase_price', 'purchase_date')
    search_fields = ('event__title', 'ticket_tier__tier_name', 'buyer__username')
    list_filter = ('payment_method', 'purchase_date')

admin.site.register(Ticket, TicketAdmin)