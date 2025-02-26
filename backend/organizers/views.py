from django.shortcuts import render
from rest_framework import viewsets
from .models import Organizer
from .serializers import OrganizerSerializer

# Create your views here.

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
