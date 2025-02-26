from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Event, TicketTier, EventPhoto
from .serializers import EventSerializer, TicketTierSerializer, EventPhotoSerializer

# This file contains the logic for handling API requests.
# It defines the views that handle requests to the /api/events/, /api/ticket-tiers/, and /api/event-photos/ endpoints.

# Each ViewSet handles a specific model and provides CRUD operations automatically (GET, POST, PUT, DELETE) 

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for events.
    
    list:
    Returns a list of all events.
    
    retrieve:
    Returns details of a specific event.
    
    create:
    Creates a new event.
    
    update:
    Updates an existing event (requires authentication).
    
    partial_update:
    Partially updates an existing event (requires authentication).
    
    destroy:
    Deletes an event (requires authentication).
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def get_permissions(self):
        """
        Allow anyone to view events, but only authenticated users to create/edit.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class TicketTierViewSet(viewsets.ModelViewSet):
    queryset = TicketTier.objects.all()
    serializer_class = TicketTierSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class EventPhotoViewSet(viewsets.ModelViewSet):
    queryset = EventPhoto.objects.all()
    serializer_class = EventPhotoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

