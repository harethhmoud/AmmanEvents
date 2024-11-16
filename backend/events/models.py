from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

CATEGORY_CHOICES = [
    ('sports', 'Sports'), #(db value, display name)
    ('music', 'Music'),
    ('cooking', 'Cooking'),
    ('art', 'Art'),
    ('fashion', 'Fashion'),
    ('dining', 'Dining'),
    ('other', 'Other'),
]

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    # all uploaded images will go to the images folder
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.title

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(rating.score for rating in ratings) / len(ratings)
        return 0 
    
class Rating(models.Model):
    # Many-to-one relationship between Rating and Event.
    # This means that many ratings can be associated with one event.
    # If an event is deleted, all associated ratings will be deleted.
    # The related_name attribute allows us to access ratings from an event instance.
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.event.title} - {self.user.username}'

    
