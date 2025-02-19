from django.db import models
from django.conf import settings
from django.db.models import Sum

class Organizer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organizer_profile'
    )
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='organizer_logos/', null=True, blank=True)
    
    # Contact info (often mirrored from the user, or stored separately)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    
    country = models.CharField(max_length=100, blank=True)
    main_city = models.CharField(max_length=100, blank=True)

    # Analytics, revenue, etc.
    analytics = models.JSONField(default=dict, blank=True)
    total_revenue = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)

    # Notifications
    notifications = models.JSONField(default=list, blank=True)
    
    # Liked events (if an organizer can also like events)
    liked_events = models.ManyToManyField('events.Event', blank=True, related_name='liked_by_organizers')
    
    # Organizer-Organizer follows
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.user.username
    
    # Example property for calculating revenue
    # Make sure to store any real transaction data in a separate table
    # or integrate with a payment system, e.g. Stripe.

    @property
    def total_revenue(self):
        result = self.transactions.aggregate(total=Sum('amount'))
        return result['total'] or 0.00
