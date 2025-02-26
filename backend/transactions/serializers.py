from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id', 'buyer', 'event', 'ticket',
            'external_payment_id', 'amount', 'status',
            'created_at', 'updated_at'
        ] 