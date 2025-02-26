from rest_framework import serializers
from .models import Ticket
from events.serializers import EventSerializer, TicketTierSerializer

class TicketSerializer(serializers.ModelSerializer):
    """
    Converts Ticket model instances to JSON and vice versa.
    Includes nested event and ticket tier data for detailed views.
    """
    # Nested serializers for related objects (read-only)
    event_details = EventSerializer(source='event', read_only=True)
    tier_details = TicketTierSerializer(source='ticket_tier', read_only=True)
    
    class Meta:
        model = Ticket
        fields = [
            'id', 'buyer', 'event', 'ticket_tier', 
            'purchase_price', 'quantity', 'payment_method',
            'purchase_date', 'event_details', 'tier_details'
        ]
        # These fields are included for write operations but not nested
        extra_kwargs = {
            'event': {'write_only': True},
            'ticket_tier': {'write_only': True}
        } 