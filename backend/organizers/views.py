from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import Organizer
from .serializers import OrganizerSerializer
from .permissions import IsOrganizerOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class OrganizerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for organizers.
    
    Provides CRUD operations for event organizer profiles with appropriate permissions.
    Public users can view organizer profiles, while only the organizer themselves can edit their profile.
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country', 'main_city']
    permission_classes = [permissions.IsAuthenticated, IsOrganizerOrReadOnly]
    
    @swagger_auto_schema(
        operation_description="Get a list of all organizers",
        manual_parameters=[
            openapi.Parameter('user', openapi.IN_QUERY, 
                description="Filter by user ID", type=openapi.TYPE_INTEGER),
            openapi.Parameter('search', openapi.IN_QUERY, 
                description="Search by name, country, or city", type=openapi.TYPE_STRING),
        ],
        responses={
            200: OrganizerSerializer(many=True),
            401: "Authentication credentials were not provided."
        }
    )
    def list(self, request, *args, **kwargs):
        """List all organizers with optional filtering"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Get details of a specific organizer",
        responses={
            200: OrganizerSerializer(),
            404: "Organizer not found"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        """Get a specific organizer profile by ID"""
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Create a new organizer profile",
        request_body=OrganizerSerializer,
        responses={
            201: OrganizerSerializer(),
            400: "Bad request - invalid data",
            401: "Authentication credentials were not provided."
        }
    )
    def create(self, request, *args, **kwargs):
        """Create a new organizer profile (requires authentication)"""
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Update an organizer profile",
        request_body=OrganizerSerializer,
        responses={
            200: OrganizerSerializer(),
            400: "Bad request - invalid data",
            401: "Authentication credentials were not provided.",
            403: "You do not have permission to perform this action.",
            404: "Organizer not found"
        }
    )
    def update(self, request, *args, **kwargs):
        """Update an organizer profile (only the owner can update)"""
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        """
        Optionally filters organizers by user ID.
        """
        queryset = Organizer.objects.all()
        
        # Filter by user if provided
        user_id = self.request.query_params.get('user')
        if user_id:
            queryset = queryset.filter(user__id=user_id)
            
        return queryset
