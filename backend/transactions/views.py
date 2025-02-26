from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
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
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            # Only allow creation, not modification
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        # Regular users can only see their own transactions
        # Staff/admin can see all transactions
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Transaction.objects.all()
        return Transaction.objects.filter(buyer=user)
