from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, TicketTier, EventPhoto
from .serializers import EventSerializer, TicketTierSerializer, EventPhotoSerializer

# This file contains the logic for handling API requests.
# It defines the views that handle requests to the /api/events/, /api/ticket-tiers/, and /api/event-photos/ endpoints.

# Each ViewSet handles a specific model and provides CRUD operations automatically (GET, POST, PUT, DELETE) 

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketTierViewSet(viewsets.ModelViewSet):
    queryset = TicketTier.objects.all()
    serializer_class = TicketTierSerializer

class EventPhotoViewSet(viewsets.ModelViewSet):
    queryset = EventPhoto.objects.all()
    serializer_class = EventPhotoSerializer

