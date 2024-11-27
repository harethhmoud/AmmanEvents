from django.db import models
from django.contrib.auth.models import AbstractUser


def user_profile_picture_upload_to(instance, filename): # so we don't dump all profile pics in the same folder
    """
    A custom function to generate file paths for profile pictures.
    Args:
        instance: The model instance (CustomUser in this case).
        filename: The original filename of the uploaded image.

    Returns:
        A string representing the file path where the image will be stored.
    """
    # Generate the file path, including the user's ID
    if not instance.id:
        return f'profile_pictures/unsaved_user/{filename}'
    return f'profile_pictures/user_{instance.id}/{filename}'

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_profile_picture_upload_to, blank=True, null=True)
    def __str__(self):
        return self.username

