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
    
    def get_queryset(self):
        """
        Optionally restricts the returned tickets to a given user,
        by filtering against a 'buyer' query parameter in the URL.
        """
        queryset = Ticket.objects.all()
        buyer_id = self.request.query_params.get('buyer')
        if buyer_id is not None:
            queryset = queryset.filter(buyer__id=buyer_id)
        return queryset
