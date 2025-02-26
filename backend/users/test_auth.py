from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class AuthenticationTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword123'
        )
        
        # URLs for token endpoints
        self.token_url = reverse('token_obtain_pair')
        self.token_refresh_url = reverse('token_refresh')
        
    def test_token_obtain(self):
        """
        Ensure we can obtain a JWT token with valid credentials.
        """
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
    def test_token_obtain_invalid_credentials(self):
        """
        Ensure token obtain fails with invalid credentials.
        """
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_token_refresh(self):
        """
        Ensure we can refresh a token.
        """
        # First obtain a token
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(self.token_url, data, format='json')
        refresh_token = response.data['refresh']
        
        # Then refresh it
        data = {
            'refresh': refresh_token
        }
        response = self.client.post(self.token_refresh_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data) 