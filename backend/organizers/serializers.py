from rest_framework import serializers
from .models import Organizer
from events.serializers import EventSerializer
from users.serializers import UserSerializer

class OrganizerSerializer(serializers.ModelSerializer):
    """
    Converts Organizer model instances to JSON and vice versa.
    Includes user details and created events.
    """
    # Nested serializers for related objects
    user_details = UserSerializer(source='user', read_only=True)
    created_events = EventSerializer(source='created_events', many=True, read_only=True)
    
    class Meta:
        model = Organizer
        fields = [
            'id', 'user', 'name', 'logo', 'contact_email',
            'contact_phone', 'country', 'main_city',
            'analytics', 'total_revenue', 'notifications',
            'created_at', 'updated_at', 'user_details',
            'created_events'
        ]
        # User ID is included for write operations but details are nested for read
        extra_kwargs = {
            'user': {'write_only': True}
        } 