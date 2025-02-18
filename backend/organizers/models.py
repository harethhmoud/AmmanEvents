from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.db.models import Sum

# Create your models here.

class Organizer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)  # Hashed password will be stored here
    country = models.CharField(max_length=100)
    main_city = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='organizer_profiles/', null=True, blank=True)
    
    # Many-to-many self-referential field to represent following relationships:
    # - "followers" are those who follow this organizer.
    # - "following" (reverse relation) are those that this organizer follows.
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    
    # Liked events: reference the Event model from the events app via a string reference.
    liked_events = models.ManyToManyField('events.Event', blank=True, related_name='liked_by')
    
    # Notifications - stored as JSON (a list of notifications)
    notifications = models.JSONField(blank=True, default=list)
    
    # Analytics - stored as JSON (for arbitrary metrics)
    analytics = models.JSONField(blank=True, default=dict)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def set_password(self, raw_password):
        """
        Hashes the provided password and updates the password field.
        """
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        """
        Returns True if the provided raw password matches the hashed one.
        """
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

    # Note: The organizer's created events can be accessed via the reverse relation because in your Event model,
    # you set created_by = ForeignKey(..., related_name='events')
    # Similarly, "upcoming events" can be derived by filtering self.events.all() based on the event date.

    @property
    def total_revenue(self):
        result = self.transactions.aggregate(total=Sum('amount'))
        return result['total'] or 0.00
