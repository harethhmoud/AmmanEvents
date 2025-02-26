from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for transactions.
    Provides CRUD operations and filtering by buyer, event, and status.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'external_payment_id']
    
    def get_queryset(self):
        """
        Optionally filters transactions by buyer, event, or status.
        """
        queryset = Transaction.objects.all()
        
        # Filter by query parameters if provided
        buyer_id = self.request.query_params.get('buyer')
        event_id = self.request.query_params.get('event')
        status = self.request.query_params.get('status')
        
        if buyer_id:
            queryset = queryset.filter(buyer__id=buyer_id)
        if event_id:
            queryset = queryset.filter(event__id=event_id)
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset
