from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from events.models import Event, EventPhoto

class EventModelTest(TestCase):
    def test_rsvp_count_property(self):
        self.assertEqual(self.event.rsvp_count, 0)

    def test_event_photo_association(self):
        # Create a dummy image file
        image_file = SimpleUploadedFile("test.jpg", b"dummydata", content_type="image/jpeg")
        photo = EventPhoto.objects.create(photo=image_file, caption="Test Caption")
        # Associate the photo with the event
        self.event.eventPhotos.add(photo)
        # Verify that the photo is associated with the event
        self.assertEqual(self.event.eventPhotos.count(), 1)
        self.assertEqual(self.event.eventPhotos.first(), photo) 