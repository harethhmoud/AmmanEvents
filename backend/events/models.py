from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
#from django.contrib.gis.db import models as gis_models
from django.db.models import Avg


def upload_to(instance, filename):
    # all uploaded images will go to directories grouped by their related instance 
    return f'images/events/{instance.id}/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)  # Simple text input for now
    #location = gis_models.PointField(geography=True, srid=4326) # srid=4326 is the standard for GPS coordinates
    # all uploaded images will go to the images folder
    image = models.ImageField(upload_to=upload_to)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')


    def __str__(self):
        return self.title

    def average_rating(self):
        return self.ratings.aggregate(Avg('score'))['score__avg'] or 0
    
class Rating(models.Model):
    # Many-to-one relationship between Rating and Event.
    # This means that many ratings can be associated with one event.
    # If an event is deleted, all associated ratings will be deleted.
    # The related_name attribute allows us to access ratings from an event instance.
    class Meta: # meta class modifies behavior of model without modifying the model itself
        unique_together = [['event', 'user']]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.event.title} - {self.user.username}'

class RSVP(models.Model):
    STATUS_CHOICES = [
        ('GOING', 'Going'),
        ('INTERESTED', 'Interested'),
    ]

    class Meta:
        unique_together = [['event', 'user']]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.event.title} - {self.user.username} - {self.get_status_display()}'
