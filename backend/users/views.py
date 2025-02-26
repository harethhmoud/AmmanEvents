from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users.
    Provides CRUD operations: GET (list & detail), POST, PUT, PATCH, DELETE
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
