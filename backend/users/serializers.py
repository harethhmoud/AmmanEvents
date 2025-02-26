from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Converts User model instances to JSON and vice versa.
    Handles password hashing during user creation.
    """
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'country', 'main_city', 'profile_pic', 'phone_number',
            'user_type'
        ]
        # Password should be write-only for security
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password) # Hashes the password
            user.save()
        return user

