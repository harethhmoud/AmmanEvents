from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from events.models import Event, TicketTier
from tickets.models import Ticket
from organizers.models import Organizer
from datetime import timedelta

User = get_user_model()

class TicketModelTest(TestCase):
    def setUp(self):
        self.buyer = User.objects.create_user(
            username="buyer", 
            password="password", 
            email="buyer@gmail.com"
        )
        self.organizer_user = User.objects.create_user(
            username="organizer", 
            password="password", 
            email="organizer@gmail.com"
        )
        self.organizer = Organizer.objects.create(
            user=self.organizer_user,
            name="Test Organizer"
        )
        self.event = Event.objects.create(
            title="Test Event",
            description="Event description",
            category="MUSIC",
            start_date=datetime.date.today(),
            location="Test Location",
            organizer=self.organizer,
            contact_email="org@gmail.com",
            contact_phone="1234567890"
        )
        self.ticket_tier = TicketTier.objects.create(
            event=self.event,
            tier_name="GA",
            price=25.00
        )

    def test_ticket_purchase_price_snapshot(self):
        """
        Verify that when a ticket is created, if purchase_price is not provided,
        it automatically takes the ticket tier's current price.
        """
        ticket = Ticket.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket_tier=self.ticket_tier,
            quantity=2,
            payment_method="CREDIT_CARD"
        )
        # Check that the purchase_price snapshot is correctly set.
        self.assertEqual(ticket.purchase_price, self.ticket_tier.price)
    
    def test_ticket_string_representation(self):
        """
        Verify that the __str__ representation for a ticket is as expected.
        """
        ticket = Ticket.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket_tier=self.ticket_tier,
            quantity=3
        )
        expected_str = f"Ticket #{ticket.id} - {self.event.title} ({self.ticket_tier.tier_name}, x3)"
        self.assertEqual(str(ticket), expected_str)

    def test_ticket_relationships(self):
        """
        Verify that the ticket correctly associates with the buyer, event, 
        and ticket tier.
        """
        ticket = Ticket.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket_tier=self.ticket_tier,
            quantity=1
        )
        self.assertEqual(ticket.buyer, self.buyer)
        self.assertEqual(ticket.event, self.event)
        self.assertEqual(ticket.ticket_tier, self.ticket_tier)

class TicketAPITests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword123'
        )
        
        # Create another user for permission testing
        self.other_user = User.objects.create_user(
            username='otheruser', 
            email='other@example.com', 
            password='testpassword123'
        )
        
        # Create organizer
        self.organizer = Organizer.objects.create(
            user=self.user,
            name='Test Organizer',
            contact_email='test@example.com'
        )
        
        # Create event
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            category='MUSIC',
            start_date='2023-12-01',
            end_date='2023-12-02',
            start_time='18:00:00',
            duration=timedelta(minutes=120),
            location='Test Location',
            organizer=self.organizer,
            contact_email='event@test.com',
            contact_phone='1234567890'
        )
        
        # Create ticket tier
        self.ticket_tier = TicketTier.objects.create(
            event=self.event,
            tier_name='General Admission',
            price=25.00
        )
        
        # Create a ticket
        self.ticket = Ticket.objects.create(
            buyer=self.user,
            event=self.event,
            ticket_tier=self.ticket_tier,
            purchase_price=25.00,
            quantity=1,
            payment_method='CREDIT_CARD'
        )
        
        # URLs
        self.tickets_url = reverse('ticket-list')
        self.ticket_detail_url = reverse('ticket-detail', args=[self.ticket.id])
        
    def test_get_tickets_list_authenticated(self):
        """
        Ensure authenticated users can retrieve their tickets.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.tickets_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # The API returns nested event data in 'event_details' instead of 'event'
        self.assertEqual(response.data[0]['event_details']['id'], self.event.id)
        
    def test_get_tickets_list_unauthenticated(self):
        """
        Ensure unauthenticated users cannot retrieve tickets.
        """
        response = self.client.get(self.tickets_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_get_ticket_detail(self):
        """
        Ensure users can retrieve details of their own tickets.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.ticket_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Update to use 'event_details' instead of 'event'
        self.assertEqual(response.data['event_details']['id'], self.event.id)
        self.assertEqual(response.data['tier_details']['id'], self.ticket_tier.id)
        
    def test_create_ticket(self):
        """
        Ensure users can purchase tickets.
        """
        self.client.force_authenticate(user=self.user)
        
        data = {
            'buyer': self.user.id,
            'event': self.event.id,
            'ticket_tier': self.ticket_tier.id,
            'purchase_price': '25.00',
            'quantity': 2,
            'payment_method': 'CREDIT_CARD'  # Use a valid payment method
        }
        response = self.client.post(self.tickets_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 2)
        
    def test_user_can_only_see_own_tickets(self):
        """
        Ensure users can only see their own tickets.
        """
        # Create a ticket for another user
        other_ticket = Ticket.objects.create(
            buyer=self.other_user,
            event=self.event,
            ticket_tier=self.ticket_tier,
            purchase_price=25.00,
            quantity=1,
            payment_method='CREDIT_CARD'
        )
        
        # Login as the first user
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.tickets_url)
        
        # Should only see own ticket, not the other user's ticket
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.ticket.id)
        
        # Try to access the other user's ticket directly
        other_ticket_url = reverse('ticket-detail', args=[other_ticket.id])
        response = self.client.get(other_ticket_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)