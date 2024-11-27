from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# admin.py configures how models are displayed in the Django admin interface.

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_picture')}),
    )
