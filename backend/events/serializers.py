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