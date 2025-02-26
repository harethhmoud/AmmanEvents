from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tickets.
    Provides CRUD operations and filtering by buyer.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # For list/retrieve, we'll filter by user in get_queryset
            permission_classes = [permissions.IsAuthenticated]
        else:
            # Only ticket owners can modify their tickets
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        # Regular users can only see their own tickets
        # Staff/admin can see all tickets
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Ticket.objects.all()
        return Ticket.objects.filter(buyer=user)
