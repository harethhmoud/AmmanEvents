from django.db import models
from django.conf import settings

# The main Event model with additional fields
class Event(models.Model):
    title = models.CharField(max_length=255)
    
    # A ManyToMany relationship to EventPhoto for storing multiple photos
    eventPhotos = models.ManyToManyField('EventPhoto', blank=True, related_name='events')
    
    description = models.TextField()
    
    CATEGORY_CHOICES = [
        ('MUSIC', 'Music'),
        ('SPORTS', 'Sports'),
        ('ART', 'Art'),
        ('FOOD', 'Food'),
        ('EDUCATION', 'Education'),
        ('TECH', 'Technology'),
        ('GAMES', 'Games'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='OTHER')
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
    
    location = models.CharField(max_length=255)
        
    # Organizer details, now linked to the Organizer app
    organizer = models.ForeignKey(
        'organizers.Organizer',
        on_delete=models.CASCADE,
        related_name='created_events',
        default=1 
    )
    
    isPromoted = models.BooleanField(default=False)
    is18_plus = models.BooleanField(default=False)
    
    likes_count = models.PositiveIntegerField(default=0)
    
    related_events = models.ManyToManyField('self', symmetrical=False, blank=True)
    
    refundPolicy = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class EventPhoto(models.Model):
    photo = models.ImageField(upload_to='event_photos/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"Photo {self.id}"


# Model for ticket tiers and their prices
class TicketTier(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='ticket_tiers'
    )
    # Ex: "General Admission", "VIP", etc.
    tier_name = models.CharField(max_length=50)
    
    # Price for the ticket tier
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return f"{self.tier_name} - {self.price}"