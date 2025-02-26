from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import Organizer

# Create your tests here.

class OrganizerAPITests(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword123'
        )
        
        self.other_user = User.objects.create_user(
            username='otheruser', 
            email='other@example.com', 
            password='testpassword123'
        )
        
        # Create organizer profile
        self.organizer = Organizer.objects.create(
            user=self.user,
            name='Test Organizer',
            contact_email='organizer@test.com',
            contact_phone='1234567890',
            country='Jordan',
            main_city='Amman'
        )
        
        # URLs
        self.organizers_url = reverse('organizer-list')
        self.organizer_detail_url = reverse('organizer-detail', args=[self.organizer.id])
        
    def test_get_organizers_list(self):
        """
        Ensure authenticated users can retrieve the list of organizers.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.organizers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Organizer')
        
    def test_get_organizer_detail(self):
        """
        Ensure authenticated users can retrieve details of an organizer.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.organizer_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Organizer')
        
    def test_create_organizer_authenticated(self):
        """
        Ensure authenticated users can create organizer profiles.
        """
        self.client.force_authenticate(user=self.other_user)
        data = {
            'user': self.other_user.id,
            'name': 'New Organizer',
            'contact_email': 'new@test.com',
            'contact_phone': '0987654321',
            'country': 'Jordan',
            'main_city': 'Amman'
        }
        response = self.client.post(self.organizers_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Organizer.objects.count(), 2)
        
    def test_create_organizer_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create organizer profiles.
        """
        data = {
            'user': self.other_user.id,
            'name': 'New Organizer',
            'contact_email': 'new@test.com'
        }
        response = self.client.post(self.organizers_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_update_own_organizer(self):
        """
        Ensure users can update their own organizer profiles.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Updated Organizer'
        }
        response = self.client.patch(self.organizer_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Organizer')
        
    def test_update_other_organizer(self):
        """
        Ensure users cannot update other users' organizer profiles.
        """
        self.client.force_authenticate(user=self.other_user)
        data = {
            'name': 'Hacked Organizer'
        }
        response = self.client.patch(self.organizer_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
