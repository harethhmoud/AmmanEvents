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

