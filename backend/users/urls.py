from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# This file defines the URLs for the UserViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 