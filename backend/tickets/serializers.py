from rest_framework import serializers
from .models import Ticket
from events.serializers import EventSerializer, TicketTierSerializer

class TicketSerializer(serializers.ModelSerializer):
    """
    Converts Ticket model instances to JSON and vice versa.
    Includes nested event and ticket tier data for detailed views.
    
    Fields:
    - id: Unique identifier for the ticket
    - buyer: User who purchased the ticket (FK to User model)
    - event: Event the ticket is for (FK to Event model)
    - ticket_tier: Tier of the ticket (FK to TicketTier model)
    - purchase_price: Price paid for the ticket
    - quantity: Number of tickets purchased
    - payment_method: Method used for payment
    - purchase_date: Date and time of purchase
    - event_details: Nested details of the event (read-only)
    - tier_details: Nested details of the ticket tier (read-only)
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