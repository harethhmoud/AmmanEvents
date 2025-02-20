from django.db import models
from django.conf import settings

class Ticket(models.Model):
    PAYMENT_CHOICES = [
        ('CREDIT_CARD', 'Credit Card'),
        ('APPLE_PAY', 'Apple Pay'),
        ('GOOGLE_PAY', 'Google Pay'),
        ('PAYPAL', 'PayPal'),
    ]

    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    ticket_tier = models.ForeignKey(
        'events.TicketTier',
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='CREDIT_CARD'
    )
    purchase_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.purchase_price:
            self.purchase_price = self.ticket_tier.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket #{self.id} - {self.event.title} ({self.ticket_tier.tier_name}, x{self.quantity})"
