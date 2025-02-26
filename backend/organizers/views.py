from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import Organizer
from .serializers import OrganizerSerializer
from .permissions import IsOrganizerOrReadOnly

# Create your views here.

class OrganizerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for organizers.
    Provides CRUD operations and filtering by name and location.
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country', 'main_city']
    permission_classes = [permissions.IsAuthenticated, IsOrganizerOrReadOnly]
    
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
