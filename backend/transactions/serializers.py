from rest_framework import serializers
from .models import Transaction
from users.serializers import UserSerializer
from events.serializers import EventSerializer
from tickets.serializers import TicketSerializer

class TransactionSerializer(serializers.ModelSerializer):
    """
    Converts Transaction model instances to JSON and vice versa.
    Includes nested buyer, event, and ticket data for detailed views.
    """
    # Nested serializers for related objects
    buyer_details = UserSerializer(source='buyer', read_only=True)
    event_details = EventSerializer(source='event', read_only=True)
    ticket_details = TicketSerializer(source='ticket', read_only=True)
    
    class Meta:
        model = Transaction
        fields = [
            'id', 'buyer', 'event', 'ticket',
            'external_payment_id', 'amount', 'status',
            'created_at', 'updated_at', 'buyer_details',
            'event_details', 'ticket_details'
        ]
        # These fields are included for write operations but not nested
        extra_kwargs = {
            'buyer': {'write_only': True},
            'event': {'write_only': True},
            'ticket': {'write_only': True}
        } 