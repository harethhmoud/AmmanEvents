from django.db import models
from django.conf import settings

# Create your models here.

class Event(models.Model):
    # Define event categories (adjust the choices as needed)
    CATEGORY_CHOICES = [
        ('MUSIC', 'Music'),
        ('SPORTS', 'Sports'),
        ('ART', 'Art'),
        ('EDUCATION', 'Education'),
        ('TECH', 'Technology'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='OTHER')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    
