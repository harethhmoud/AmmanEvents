from rest_framework import serializers
from .models import Event, TicketTier, EventPhoto

# Serializer file that converts DB objects to JSON and back

class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPhoto
        fields = ['id', 'photo', 'caption']

class TicketTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTier
        fields = ['id', 'tier_name', 'price']

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.
    Includes nested ticket tiers and event photos.
    
    Example response:
    {
        "id": 1,
        "title": "Summer Music Festival",
        "description": "A weekend of amazing music performances",
        "category": "music",
        "start_date": "2023-07-15",
        "end_date": "2023-07-17",
        "start_time": "16:00:00",
        "duration": 180,
        "location": "City Park, Amman",
        "organizer": 1,
        "isPromoted": true,
        "is18_plus": false,
        "contact_email": "info@festival.com",
        "contact_phone": "+962 79 123 4567",
        "likes_count": 245,
        "refundPolicy": "Full refund up to 7 days before the event",
        "schedule": "Day 1: Rock bands, Day 2: Pop artists, Day 3: Local talent",
        "tags": ["music", "festival", "summer"],
        "ticket_tiers": [
            {
                "id": 1,
                "tier_name": "General Admission",
                "price": 25.00
            },
            {
                "id": 2,
                "tier_name": "VIP",
                "price": 75.00
            }
        ],
        "eventPhotos": [
            {
                "id": 1,
                "photo": "/media/events/festival1.jpg",
                "caption": "Main stage"
            }
        ]
    }
    """
    ticket_tiers = TicketTierSerializer(many=True, read_only=True)
    eventPhotos = EventPhotoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'category', 
            'eventPhotoURLs', 'start_date', 'end_date', 
            'start_time', 'duration', 'location', 
            'organizer', 'isPromoted', 'is18_plus',
            'contact_email', 'contact_phone', 'likes_count',
            'refundPolicy', 'schedule', 'tags',
            'ticket_tiers', 'eventPhotos'
        ] 