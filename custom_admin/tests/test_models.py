from django.test import TestCase
from django.contrib.auth.models import User
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from datetime import date, timedelta

class BookingModelTest(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create test room category
        self.room_category = RoomCategory.objects.create(
            name='Test Category',
            description='Test Description',
            price=100.00
        )
        
        # Create test room
        self.room = Room.objects.create(
            name='Test Room',
            category=self.room_category,
            is_available=True
        )
        
        # Create test booking
        self.booking = Booking.objects.create(
            user=self.user,
            room_category=self.room_category,
            room=self.room,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            total_price=200.00
        )

    def test_booking_creation(self):
        """Test that a booking can be created"""
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.room_category, self.room_category)
        self.assertEqual(self.booking.room, self.room)
        self.assertEqual(self.booking.total_price, 200.00)
        self.assertFalse(self.booking.is_paid)
        self.assertIsNotNone(self.booking.booking_number)

    def test_booking_str_representation(self):
        """Test the string representation of the booking"""
        expected_str = f"{self.user.username} - {self.booking.booking_number} ({self.booking.check_in} to {self.booking.check_out})"
        self.assertEqual(str(self.booking), expected_str)

    def test_booking_dates_validation(self):
        """Test that booking dates are validated correctly"""
        with self.assertRaises(Exception):
            Booking.objects.create(
                user=self.user,
                room_category=self.room_category,
                room=self.room,
                check_in=date.today() + timedelta(days=3),
                check_out=date.today() + timedelta(days=2),
                total_price=200.00
            ) 