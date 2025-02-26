from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        """
        Test that a regular user can be created with the proper fields
        and that the password is hashed.
        """
        user = User.objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="securepassword"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertTrue(user.check_password("securepassword"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_user_str_representation(self):
        """
        Test the string representation of the user.
        Adjust this test if your __str__ method returns something different.
        """
        user = User.objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="securepassword"
        )
        self.assertEqual(str(user), "testuser")

    def test_create_superuser(self):
        """
        Test that a superuser can be created and has is_staff and is_superuser True.
        """
        admin = User.objects.create_superuser(
            username="admin",
            email="admin@gmail.com",
            password="adminpassword"
        )
        self.assertEqual(admin.username, "admin")
        self.assertEqual(admin.email, "admin@gmail.com")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

class UserRegistrationTests(APITestCase):
    def setUp(self):
        # URL for user registration
        self.register_url = reverse('register')
        
    def test_user_registration(self):
        """
        Ensure we can register a new user.
        """
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'first_name': 'New',
            'last_name': 'User',
            'country': 'Jordan',
            'main_city': 'Amman'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'newuser')
        
    def test_user_registration_invalid_data(self):
        """
        Ensure user registration fails with invalid data.
        """
        # Missing required fields
        data = {
            'username': 'newuser',
            # Missing email and password
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Invalid email format
        data = {
            'username': 'newuser',
            'email': 'invalid-email',
            'password': 'newpassword123'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
