from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, TicketTier, EventPhoto
from .serializers import EventSerializer, TicketTierSerializer, EventPhotoSerializer

# This file contains the logic for handling API requests.
# It defines the views that handle requests to the /api/events/, /api/ticket-tiers/, and /api/event-photos/ endpoints.

# ViewSets provide CRUD operations automatically

# Handles /api/events/ endpoints
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Handles /api/ticket-tiers/ endpoints
class TicketTierViewSet(viewsets.ModelViewSet):
    queryset = TicketTier.objects.all()
    serializer_class = TicketTierSerializer

# Handles /api/event-photos/ endpoints
class EventPhotoViewSet(viewsets.ModelViewSet):
    queryset = EventPhoto.objects.all()
    serializer_class = EventPhotoSerializer

