from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from bookings.models import Booking, Room, RoomCategory
from payments.models import Payment

class PaymentModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create a room category
        self.room_category = RoomCategory.objects.create(
            name='Deluxe',
            description='Deluxe room category',
            price=100.00
        )
        
        # Create a room
        self.room = Room.objects.create(
            name='Room 101',
            category=self.room_category,
            is_available=True
        )
        
        # Create a test booking
        self.booking = Booking.objects.create(
            user=self.test_user,
            room=self.room,
            room_category=self.room_category,
            check_in=timezone.now().date(),
            check_out=timezone.now().date(),
            total_price=200.00
        )
        
        # Create a test payment
        self.payment = Payment.objects.create(
            booking=self.booking,
            stripe_payment_intent='test_payment_intent_123',
            amount=100.00,
            status='completed'
        )

    def test_payment_creation(self):
        """Test that a payment can be created"""
        self.assertEqual(self.payment.booking, self.booking)
        self.assertEqual(self.payment.stripe_payment_intent, 'test_payment_intent_123')
        self.assertEqual(self.payment.amount, 100.00)
        self.assertEqual(self.payment.status, 'completed')
        self.assertIsNotNone(self.payment.timestamp)

    def test_payment_str_representation(self):
        """Test the string representation of the payment"""
        expected_str = f"Payment for booking {self.booking.id} - completed"
        self.assertEqual(str(self.payment), expected_str)

    def test_payment_amount_validation(self):
        """Test that payment amount cannot be negative"""
        with self.assertRaises(Exception):
            Payment.objects.create(
                booking=self.booking,
                stripe_payment_intent='test_payment_intent_456',
                amount=-100.00,
                status='completed'
            ) 