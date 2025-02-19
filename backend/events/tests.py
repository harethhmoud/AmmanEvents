from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime
from django.core.files.uploadedfile import SimpleUploadedFile

from organizers.models import Organizer
from .models import Event, TicketTier, EventPhoto

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