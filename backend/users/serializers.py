from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Converts User model instances to JSON and vice versa.
    Handles password hashing during user creation.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'country', 'main_city', 'phone_number', 'user_type']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},  # Make email required
        }
    
    def validate_email(self, value):
        """
        Check that the email is valid.
        """
        if '@' not in value:
            raise serializers.ValidationError("Enter a valid email address.")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

