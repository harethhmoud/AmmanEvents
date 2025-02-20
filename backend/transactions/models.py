from django.db import models
from django.conf import settings
# Import Organizer from the organizers app
from organizers.models import Organizer

class Transaction(models.Model):
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1  # Use the primary key of a valid user
    )
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    ticket = models.ForeignKey('tickets.Ticket', on_delete=models.CASCADE, null=True, blank=True)

    # Reference from payment processor (probably gonna be a stripe id)
    external_payment_id = models.CharField(max_length=255, blank=True)

    amount = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction #{self.id} - Buyer: {self.buyer} - Amount: {self.amount}"
