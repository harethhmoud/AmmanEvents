from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

# This file defines the URLs for the TicketViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 