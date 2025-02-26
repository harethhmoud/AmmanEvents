from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet

# This file defines the URLs for the TransactionViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 