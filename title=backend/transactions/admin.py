from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'event', 'amount', 'status', 'created_at')
    search_fields = ('buyer__username', 'event__title', 'external_payment_id')
    list_filter = ('status', 'created_at')

admin.site.register(Transaction, TransactionAdmin) 