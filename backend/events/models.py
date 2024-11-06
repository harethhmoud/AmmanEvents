from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    # all uploaded images will go to the images folder
    image = models.ImageField(upload_to='images/')
