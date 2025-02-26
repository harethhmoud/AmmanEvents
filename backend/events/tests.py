from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from organizers.models import Organizer
from .models import Event, TicketTier, EventPhoto
from users.models import User

User = get_user_model()

class EventModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", 
            password="password123", 
            email="testuser@gmail.com"
        )
        self.organizer = Organizer.objects.create(
            user=self.user,
            name="Test Organizer"
        )
        self.event = Event.objects.create(
            title="Test Event",
            description="A test event description",
            category="MUSIC",
            start_date=datetime.date(2023, 10, 1),
            location="Test Location",
            organizer=self.organizer,
            contact_email="contact@test.com",
            contact_phone="1234567890"
        )
        self.related_event = Event.objects.create(
            title="Related Event",
            description="A related event description",
            category="MUSIC",
            start_date=datetime.date(2023, 10, 2),
            location="Another Location",
            organizer=self.organizer,
            contact_email="related@test.com",
            contact_phone="0987654321"
        )
        self.event.related_events.add(self.related_event)
        
        self.ticket_tier = TicketTier.objects.create(
            event=self.event,
            tier_name="GA", 
            price=20.00
        )

    def test_event_str(self):
        self.assertEqual(str(self.event), "Test Event")

    def test_event_category(self):
        self.assertEqual(self.event.category, "MUSIC")

    def test_event_default_json_fields(self):
        self.assertEqual(self.event.eventPhotoURLs, [])
        self.assertEqual(self.event.schedule, [])
        self.assertEqual(self.event.tags, [])

    def test_related_events(self):
        self.assertEqual(self.event.related_events.count(), 1)
        self.assertIn(self.related_event, self.event.related_events.all())

    def test_ticket_tier_relationship(self):
        self.assertEqual(self.event.ticket_tiers.count(), 1)
        self.assertEqual(self.event.ticket_tiers.first(), self.ticket_tier)

    def test_rsvp_count_property(self):
        self.assertEqual(self.event.rsvp_count, 0)

    def test_event_photo_association(self):
        image_file = SimpleUploadedFile("test.jpg", b"dummydata", content_type="image/jpeg")
        # Create an EventPhoto instance.
        photo = EventPhoto.objects.create(photo=image_file, caption="Test Caption")
        self.event.eventPhotos.add(photo)
        self.assertEqual(self.event.eventPhotos.count(), 1)
        self.assertEqual(self.event.eventPhotos.first(), photo)

class EventAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword123'
        )
        
        # Create an organizer for the user
        self.organizer = Organizer.objects.create(
            user=self.user,
            name='Test Organizer',
            contact_email='test@example.com'
        )
        
        # Create a test event
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            category='music',
            start_date='2023-12-01',
            end_date='2023-12-02',
            location='Test Location',
            organizer=self.organizer  # Use organizer instance, not user
        )
        
        # URL for events list
        self.events_url = reverse('event-list')
        # URL for specific event detail
        self.event_detail_url = reverse('event-detail', args=[self.event.id])
        
    def test_get_events_list(self):
        """
        Ensure we can retrieve the events list.
        """
        response = self.client.get(self.events_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Event')
    
    def test_get_event_detail(self):
        """
        Ensure we can retrieve a specific event.
        """
        response = self.client.get(self.event_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Event')
    
    def test_create_event_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create events.
        """
        data = {
            'title': 'New Event',
            'description': 'New Description',
            'category': 'sports',
            'start_date': '2023-12-15',
            'end_date': '2023-12-16',
            'location': 'New Location',
            'organizer': self.user.id
        }
        response = self.client.post(self.events_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_event_authenticated(self):
        """
        Ensure authenticated users can create events.
        """
        # Authenticate the user
        self.client.force_authenticate(user=self.user)
        
        # Use a valid category from your model's choices
        # Based on your EventModelTest, it seems 'MUSIC' (uppercase) is a valid choice
        data = {
            'title': 'New Event',
            'description': 'New Description',
            'category': 'MUSIC',  # Use uppercase as defined in your model
            'start_date': '2023-12-15',
            'end_date': '2023-12-16',
            'start_time': '18:00:00',
            'duration': 120,
            'location': 'New Location',
            'organizer': self.organizer.id,
            'contact_email': 'event@test.com',
            'contact_phone': '1234567890',
            'refundPolicy': 'No refunds',
            'tags': ['music', 'concert']
        }
        response = self.client.post(self.events_url, data, format='json')
        
        # If the test still fails, print the response content for debugging
        if response.status_code != 201:
            print(f"Response content: {response.content}")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)
        self.assertEqual(Event.objects.get(id=2).title, 'New Event')