from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # AbstractUser already provides:
    # id, username, email, password, etc.

    first_name = models.CharField(max_length=255, blank=True) 
    last_name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)
    main_city = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    liked_events = models.ManyToManyField('events.Event', blank=True, related_name='liked_by_users')
    upcoming_events = models.ManyToManyField('events.Event', blank=True, related_name='upcoming_for_users')
    attended_events = models.ManyToManyField('events.Event', blank=True, related_name='attended_by_users')

    organizers_followed = models.ManyToManyField(
        'organizers.Organizer',
        blank=True,
        related_name='followed_by_users'
    )

    notifications = models.JSONField(default=list, blank=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    USER_TYPE_CHOICES = [
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
    ]
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default='attendee'
    )

    def __str__(self):
        return self.username
