from django.test import TestCase
from django.contrib.auth.models import User
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from datetime import date, timedelta
from django.core.exceptions import ValidationError

class BookingModelTest(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
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
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            total_price=200.00
        )

    def test_booking_creation(self):
        """Test that a booking is created correctly"""
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.room_category, self.room_category)
        self.assertEqual(self.booking.room, self.room)
        self.assertEqual(self.booking.total_price, 200.00)
        self.assertFalse(self.booking.is_paid)
        self.assertFalse(self.booking.is_cancelled)
        self.assertIsNotNone(self.booking.booking_number)

    def test_booking_number_generation(self):
        """Test that booking numbers are unique and 6 digits"""
        booking2 = Booking.objects.create(
            user=self.user,
            room_category=self.room_category,
            room=self.room,
            check_in=date.today() + timedelta(days=3),
            check_out=date.today() + timedelta(days=5),
            total_price=200.00
        )
        
        self.assertNotEqual(self.booking.booking_number, booking2.booking_number)
        self.assertEqual(len(self.booking.booking_number), 6)
        self.assertTrue(self.booking.booking_number.isdigit())

    def test_booking_str_representation(self):
        """Test the string representation of a booking"""
        expected_str = f"{self.user.username} - {self.booking.booking_number} ({self.booking.check_in} to {self.booking.check_out})"
        self.assertEqual(str(self.booking), expected_str)

    def test_booking_dates_validation(self):
        """Test that check-out date must be after check-in date"""
        with self.assertRaises(ValidationError):
            Booking.objects.create(
                user=self.user,
                room_category=self.room_category,
                room=self.room,
                check_in=date.today() + timedelta(days=2),
                check_out=date.today(),
                total_price=200.00
            ) 