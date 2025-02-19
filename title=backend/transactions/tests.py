from django.test import TestCase
from django.contrib.auth import get_user_model
import datetime

from organizers.models import Organizer
from events.models import Event, TicketTier
from tickets.models import Ticket
from transactions.models import Transaction

User = get_user_model()

class TransactionModelTest(TestCase):
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
        # Create an event requiring an organizer.
        self.event = Event.objects.create(
            title="Test Event",
            description="Test event description",
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
            price=30.00
        )
        # Create a ticket for this event.
        self.ticket = Ticket.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket_tier=self.ticket_tier,
            quantity=1,
            payment_method="CREDIT_CARD"
        )
        # Create a transaction using the buyer, event, and ticket.
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
        # Verify that the Transaction correctly relates to buyer, event, and ticket.
        self.assertEqual(self.transaction.buyer, self.buyer)
        self.assertEqual(self.transaction.event, self.event)
        self.assertEqual(self.transaction.ticket, self.ticket)

    def test_transaction_default_status(self):
        # Creating a transaction without explicitly setting a status should default to "pending".
        transaction_default = Transaction.objects.create(
            buyer=self.buyer,
            event=self.event,
            ticket=self.ticket,
            amount=30.00
        )
        self.assertEqual(transaction_default.status, "pending")

    def test_transaction_external_payment_id_field(self):
        # Verify that the external_payment_id field can be left blank.
        self.transaction.external_payment_id = ""
        self.transaction.save()
        self.assertEqual(self.transaction.external_payment_id, "") 