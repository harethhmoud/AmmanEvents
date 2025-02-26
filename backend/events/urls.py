from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TicketTierViewSet, EventPhotoViewSet

# Router automatically creates URL patterns for our ViewSets
router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'ticket-tiers', TicketTierViewSet)
router.register(r'event-photos', EventPhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 