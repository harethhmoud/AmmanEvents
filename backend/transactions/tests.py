from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import timedelta

from organizers.models import Organizer
from events.models import Event, TicketTier
from tickets.models import Ticket
from transactions.models import Transaction
from users.models import User

User = get_user_model()

class TransactionModelTest(TestCase):
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
            description="Test event description",
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
            price=30.00
        )
        self.ticket = Ticket.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket_tier=self.ticket_tier,
            quantity=1,
            payment_method="CREDIT_CARD"
        )
        self.transaction = Transaction.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket=self.ticket,
            external_payment_id="EXT123",
            amount=30.00,
            status="completed"
        )

    def test_transaction_string_representation(self):
        expected_str = f"Transaction #{self.transaction.id} - Buyer: {self.buyer} - Amount: {self.transaction.amount}"
        self.assertEqual(str(self.transaction), expected_str)

    def test_transaction_relationships(self):
        self.assertEqual(self.transaction.buyer, self.buyer)
        self.assertEqual(self.transaction.event, self.event)
        self.assertEqual(self.transaction.ticket, self.ticket)

    def test_transaction_default_status(self):
        transaction_default = Transaction.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket=self.ticket,
            amount=30.00
        )
        self.assertEqual(transaction_default.status, "pending")

    def test_transaction_external_payment_id_field(self):
        self.transaction.external_payment_id = ""
        self.transaction.save()
        self.assertEqual(self.transaction.external_payment_id, "")

class TransactionAPITests(APITestCase):
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
            payment_method='credit_card'
        )
        
        # Create a transaction
        self.transaction = Transaction.objects.create(
            buyer=self.user,
            event=self.event,
            amount=25.00,
            status='completed',
            external_payment_id='test123'
        )
        
        # URLs
        self.transactions_url = reverse('transaction-list')
        self.transaction_detail_url = reverse('transaction-detail', args=[self.transaction.id])
        
    def test_get_transactions_list_authenticated(self):
        """
        Ensure authenticated users can retrieve their transactions.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.transactions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # Check that the event details are included
        self.assertEqual(response.data[0]['event_details']['id'], self.event.id)
        
    def test_get_transactions_list_unauthenticated(self):
        """
        Ensure unauthenticated users cannot retrieve transactions.
        """
        response = self.client.get(self.transactions_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_get_transaction_detail(self):
        """
        Ensure users can retrieve details of their own transactions.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.transaction_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the event details are included
        self.assertEqual(response.data['event_details']['id'], self.event.id)
        self.assertEqual(response.data['amount'], '25.00')
        
    def test_create_transaction(self):
        """
        Ensure users can create transactions.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'buyer': self.user.id,
            'event': self.event.id,
            'amount': 50.00,
            'status': 'pending',
            'external_payment_id': 'test456'
        }
        response = self.client.post(self.transactions_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)
        
    def test_user_can_only_see_own_transactions(self):
        """
        Ensure users can only see their own transactions.
        """
        # Create a transaction for another user
        other_transaction = Transaction.objects.create(
            buyer=self.other_user,
            event=self.event,
            amount=25.00,
            status='completed',
            external_payment_id='test789'
        )
        
        # Login as the first user
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.transactions_url)
        
        # Should only see own transaction, not the other user's transaction
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.transaction.id)
        
        # Try to access the other user's transaction directly
        other_transaction_url = reverse('transaction-detail', args=[other_transaction.id])
        response = self.client.get(other_transaction_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

