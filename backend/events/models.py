from django.db import models
from django.conf import settings
from organizers.models import Organizer
import datetime

class Event(models.Model):
    title = models.CharField(max_length=255)
    
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
    
    eventPhotoURLs = models.JSONField(default=list, blank=True)
    
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    location = models.CharField(max_length=255)
        
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='created_events')
    
    isPromoted = models.BooleanField(default=False)
    is18_plus = models.BooleanField(default=False)
    
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    
    likes_count = models.PositiveIntegerField(default=0)
    
    related_events = models.ManyToManyField('self', blank=True, symmetrical=False)
    
    refundPolicy = models.TextField(blank=True, null=True)
    
    schedule = models.JSONField(default=list, blank=True)
    
    tags = models.JSONField(default=list, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    @property
    def rsvp_count(self):
        return 0


class EventPhoto(models.Model):
    photo = models.ImageField(upload_to='event_photos/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"Photo {self.id}"

class TicketTier(models.Model):
    TIER_CHOICES = [
        ('GA', 'General Admission'),
        ('VIP', 'VIP'),
        ('EARLY_BIRD', 'Early Bird'),
        ('OTHER', 'Other'),
    ]
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name='ticket_tiers',
        null=True,
        blank=True
    )
    tier_name = models.CharField(
        max_length=50,
        choices=TIER_CHOICES,
        default='GA'
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return f"{self.tier_name} - {self.price}"