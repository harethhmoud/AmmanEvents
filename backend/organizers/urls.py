from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizerViewSet

# This file defines the URLs for the OrganizerViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'organizers', OrganizerViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 