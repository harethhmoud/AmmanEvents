from django.db import models
from django.conf import settings
# Import Organizer from the organizers app
from organizers.models import Organizer

class Transaction(models.Model):
    organizer = models.ForeignKey(
        Organizer, on_delete=models.CASCADE, related_name='transactions'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='success')
    # Optional: If integrating with external gateways, store a transaction reference ID
    # external_reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.organizer.username} - {self.amount} on {self.timestamp}"
