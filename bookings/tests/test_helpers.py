from django.test import TestCase
from django.contrib.auth.models import User
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from bookings.helpers import check_room_availability
from datetime import date, timedelta

class RoomAvailabilityTest(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test room categories
        self.room_category1 = RoomCategory.objects.create(
            name='Test Category 1',
            description='Test Description 1',
            price=100.00
        )
        self.room_category2 = RoomCategory.objects.create(
            name='Test Category 2',
            description='Test Description 2',
            price=150.00
        )
        
        # Create test rooms for category 1
        self.room1 = Room.objects.create(
            name='Test Room 1',
            category=self.room_category1,
            is_available=True
        )
        self.room2 = Room.objects.create(
            name='Test Room 2',
            category=self.room_category1,
            is_available=True
        )
        
        # Create test rooms for category 2
        self.room3 = Room.objects.create(
            name='Test Room 3',
            category=self.room_category2,
            is_available=True
        )
        self.room4 = Room.objects.create(
            name='Test Room 4',
            category=self.room_category2,
            is_available=True
        )

    def test_room_availability_with_no_bookings(self):
        """Test room availability when there are no bookings"""
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)

    def test_room_availability_with_one_booking(self):
        """Test room availability when one room is booked"""
        # Create a booking for room1
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            is_paid=True,
            total_price=200.00
        )
        
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)  # Should still be available as we have room2

    def test_room_availability_with_all_rooms_booked(self):
        """Test room availability when all rooms are booked"""
        # Create bookings for both rooms
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            is_paid=True,
            total_price=200.00
        )
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room2,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            is_paid=True,
            total_price=200.00
        )
        
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertFalse(is_available)

    def test_room_availability_with_cancelled_booking(self):
        """Test room availability when a booking is cancelled"""
        # Create a cancelled booking
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            is_paid=True,
            is_cancelled=True,
            total_price=200.00
        )
        
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)  # Should be available as booking is cancelled

    def test_room_availability_with_overlapping_bookings(self):
        """Test room availability with overlapping bookings"""
        # Create a booking that overlaps with the test period
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            is_paid=True,
            total_price=200.00
        )
        
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)  # Should be available as we have room2

    def test_room_availability_with_non_overlapping_bookings(self):
        """Test room availability with non-overlapping bookings"""
        # Create a booking that doesn't overlap with the test period
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today() + timedelta(days=3),
            check_out=date.today() + timedelta(days=5),
            is_paid=True,
            total_price=200.00
        )
        
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)  # Should be available as booking doesn't overlap

    def test_room_availability_with_multiple_overlapping_bookings(self):
        """Test room availability with multiple overlapping bookings"""
        # Create multiple overlapping bookings
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=3),
            is_paid=True,
            total_price=300.00
        )
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room2,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=4),
            is_paid=True,
            total_price=300.00
        )
        
        check_in = date.today() + timedelta(days=2)
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertFalse(is_available)  # Should not be available as both rooms are booked

    def test_room_availability_with_same_day_checkout_checkin(self):
        """Test room availability when check-out equals another booking's check-in"""
        # Create a booking
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            is_paid=True,
            total_price=200.00
        )
        
        # Try to book starting on the same day as the previous booking's check-out
        check_in = date.today() + timedelta(days=2)
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)  # Should be available as check-in equals previous check-out

    def test_room_availability_with_unpaid_bookings(self):
        """Test room availability with unpaid bookings"""
        # Create an unpaid booking
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            is_paid=False,
            total_price=200.00
        )
        
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)  # Should be available as booking is not paid

    def test_room_availability_with_different_categories(self):
        """Test room availability with bookings in different categories"""
        # Create a booking in category 1
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            is_paid=True,
            total_price=200.00
        )
        
        check_in = date.today()
        check_out = check_in + timedelta(days=2)
        
        # Check availability in category 2
        is_available = check_room_availability(self.room_category2.id, check_in, check_out)
        self.assertTrue(is_available)  # Should be available as booking is in different category

    def test_room_availability_with_long_term_bookings(self):
        """Test room availability with long-term bookings"""
        # Create a long-term booking
        Booking.objects.create(
            user=self.user,
            room_category=self.room_category1,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=7),
            is_paid=True,
            total_price=700.00
        )
        
        # Try to book during the long-term booking
        check_in = date.today() + timedelta(days=3)
        check_out = check_in + timedelta(days=2)
        
        is_available = check_room_availability(self.room_category1.id, check_in, check_out)
        self.assertTrue(is_available)  # Should be available as we have room2 