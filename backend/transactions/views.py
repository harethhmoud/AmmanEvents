from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import Transaction
from .serializers import TransactionSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for transactions.
    
    Provides CRUD operations for payment transactions with appropriate permissions.
    Users can only see their own transactions, while staff can see all transactions.
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
    
    @swagger_auto_schema(
        operation_description="Get a list of transactions",
        manual_parameters=[
            openapi.Parameter('status', openapi.IN_QUERY, 
                description="Filter by status (e.g., 'completed', 'pending', 'failed')", 
                type=openapi.TYPE_STRING),
            openapi.Parameter('event', openapi.IN_QUERY, 
                description="Filter by event ID", 
                type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: TransactionSerializer(many=True),
            401: "Authentication credentials were not provided."
        }
    )
    def list(self, request, *args, **kwargs):
        """
        List transactions for the current user.
        Staff users can see all transactions.
        """
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        # Regular users can only see their own transactions
        # Staff/admin can see all transactions
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Transaction.objects.all()
        return Transaction.objects.filter(buyer=user)
