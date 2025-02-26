from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Event, TicketTier, EventPhoto
from .serializers import EventSerializer, TicketTierSerializer, EventPhotoSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# This file contains the logic for handling API requests.
# It defines the views that handle requests to the /api/events/, /api/ticket-tiers/, and /api/event-photos/ endpoints.

# Each ViewSet handles a specific model and provides CRUD operations automatically (GET, POST, PUT, DELETE) 

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for events.
    
    Provides complete CRUD functionality for events with appropriate permissions.
    Public users can view events, while authenticated users can create and manage events.
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
    
    @swagger_auto_schema(
        operation_description="Get a list of all events",
        manual_parameters=[
            openapi.Parameter('category', openapi.IN_QUERY, 
                description="Filter by category (e.g., 'music', 'sports')", type=openapi.TYPE_STRING),
            openapi.Parameter('location', openapi.IN_QUERY, 
                description="Filter by location", type=openapi.TYPE_STRING),
            openapi.Parameter('start_date', openapi.IN_QUERY, 
                description="Filter by start date (YYYY-MM-DD)", type=openapi.TYPE_STRING),
        ],
        responses={
            200: EventSerializer(many=True),
            401: "Authentication credentials were not provided."
        }
    )
    def list(self, request, *args, **kwargs):
        """List all events with optional filtering"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Get details of a specific event",
        responses={
            200: EventSerializer(),
            404: "Event not found"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        """Get a specific event by ID"""
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Create a new event",
        request_body=EventSerializer,
        responses={
            201: EventSerializer(),
            400: "Bad request - invalid data",
            401: "Authentication credentials were not provided."
        }
    )
    def create(self, request, *args, **kwargs):
        """Create a new event (requires authentication)"""
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Update an existing event",
        request_body=EventSerializer,
        responses={
            200: EventSerializer(),
            400: "Bad request - invalid data",
            401: "Authentication credentials were not provided.",
            404: "Event not found"
        }
    )
    def update(self, request, *args, **kwargs):
        """Update an event (requires authentication)"""
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Delete an event",
        responses={
            204: "No content - successfully deleted",
            401: "Authentication credentials were not provided.",
            404: "Event not found"
        }
    )
    def destroy(self, request, *args, **kwargs):
        """Delete an event (requires authentication)"""
        return super().destroy(request, *args, **kwargs)

class TicketTierViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ticket tiers.
    
    Provides CRUD operations for ticket tiers associated with events.
    Public users can view ticket tiers, while authenticated users can create and manage them.
    """
    queryset = TicketTier.objects.all()
    serializer_class = TicketTierSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @swagger_auto_schema(
        operation_description="Get a list of all ticket tiers",
        manual_parameters=[
            openapi.Parameter('event', openapi.IN_QUERY, 
                description="Filter by event ID", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: TicketTierSerializer(many=True),
            401: "Authentication credentials were not provided."
        }
    )
    def list(self, request, *args, **kwargs):
        """List all ticket tiers with optional filtering by event"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Get details of a specific ticket tier",
        responses={
            200: TicketTierSerializer(),
            404: "Ticket tier not found"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        """Get a specific ticket tier by ID"""
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Create a new ticket tier",
        request_body=TicketTierSerializer,
        responses={
            201: TicketTierSerializer(),
            400: "Bad request - invalid data",
            401: "Authentication credentials were not provided."
        }
    )
    def create(self, request, *args, **kwargs):
        """Create a new ticket tier (requires authentication)"""
        return super().create(request, *args, **kwargs)

class EventPhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint for event photos.
    
    Provides CRUD operations for photos associated with events.
    Public users can view photos, while authenticated users can upload and manage them.
    """
    queryset = EventPhoto.objects.all()
    serializer_class = EventPhotoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @swagger_auto_schema(
        operation_description="Get a list of all event photos",
        manual_parameters=[
            openapi.Parameter('event', openapi.IN_QUERY, 
                description="Filter by event ID", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: EventPhotoSerializer(many=True),
            401: "Authentication credentials were not provided."
        }
    )
    def list(self, request, *args, **kwargs):
        """List all event photos with optional filtering by event"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Upload a new event photo",
        request_body=EventPhotoSerializer,
        responses={
            201: EventPhotoSerializer(),
            400: "Bad request - invalid data",
            401: "Authentication credentials were not provided."
        }
    )
    def create(self, request, *args, **kwargs):
        """Upload a new event photo (requires authentication)"""
        return super().create(request, *args, **kwargs)

