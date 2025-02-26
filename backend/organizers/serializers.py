from rest_framework import serializers
from .models import Organizer

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = [
            'id', 'user', 'name', 'logo', 'contact_email',
            'contact_phone', 'country', 'main_city',
            'analytics', 'total_revenue', 'notifications',
            'created_at', 'updated_at'
        ] 