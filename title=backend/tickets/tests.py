from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime

from events.models import Event, TicketTier
from tickets.models import Ticket
from organizers.models import Organizer

User = get_user_model()

class TicketModelTest(TestCase):
    def setUp(self):
        # Create a buyer and an organizer user.
        self.buyer = User.objects.create_user(
            username="buyer", 
            password="password", 
            email="buyer@example.com"
        )
        self.organizer_user = User.objects.create_user(
            username="organizer", 
            password="password", 
            email="organizer@example.com"
        )
        # Create an Organizer instance linked to the organizer user.
        self.organizer = Organizer.objects.create(
            user=self.organizer_user,
            name="Test Organizer"
        )
        # Create an event, requiring an organizer.
        self.event = Event.objects.create(
            title="Test Event",
            description="Event description",
            category="MUSIC",
            start_date=datetime.date.today(),
            location="Test Location",
            organizer=self.organizer,
            contact_email="org@example.com",
            contact_phone="1234567890"
        )
        # Create a ticket tier for the event.
        self.ticket_tier = TicketTier.objects.create(
            event=self.event,
            tier_name="GA",  # General Admission as defined in choices.
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