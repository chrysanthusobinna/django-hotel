from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from bookings.admin import BookingAdmin
from datetime import date, timedelta

class MockRequest:
    def __init__(self):
        self.session = {}
        self._messages = FallbackStorage(self)
        self.META = {}
        self.COOKIES = {}
        self.user = None

    def get_host(self):
        return 'testserver'

class MockSuperUser:
    def has_perm(self, perm):
        return True

class BookingAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = BookingAdmin(Booking, self.site)
        
        # Create test user
        self.user = User.objects.create_superuser(
            username='admin',
            password='adminpass123',
            email='admin@example.com'
        )
        
        # Create test room category
        self.room_category = RoomCategory.objects.create(
            name='Test Category',
            description='Test Description',
            price=100.00
        )
        
        # Create test rooms
        self.room1 = Room.objects.create(
            name='Test Room 1',
            category=self.room_category,
            is_available=True
        )
        self.room2 = Room.objects.create(
            name='Test Room 2',
            category=self.room_category,
            is_available=True
        )
        
        # Create test booking
        self.booking = Booking.objects.create(
            user=self.user,
            room_category=self.room_category,
            room=self.room1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=2),
            total_price=200.00
        )

    def test_list_display(self):
        """Test that list_display contains all required fields"""
        self.assertEqual(
            self.admin.list_display,
            ('booking_number', 'user', 'room_category', 'room', 'check_in', 
             'check_out', 'is_paid', 'is_cancelled', 'created_at')
        )

    def test_list_filter(self):
        """Test that list_filter contains all required fields"""
        self.assertEqual(
            self.admin.list_filter,
            ('is_paid', 'is_cancelled', 'check_in', 'check_out', 'room_category')
        )

    def test_search_fields(self):
        """Test that search_fields contains all required fields"""
        self.assertEqual(
            self.admin.search_fields,
            ('booking_number', 'user__username', 'room__name', 'room_category__name')
        )

    def test_readonly_fields(self):
        """Test that readonly_fields contains all required fields"""
        self.assertEqual(
            self.admin.readonly_fields,
            ('booking_number', 'created_at')
        )

    def test_cancel_bookings_action(self):
        """Test the cancel_bookings admin action"""
        request = MockRequest()
        request.user = MockSuperUser()
        
        # Add middleware
        SessionMiddleware(lambda r: None).process_request(request)
        MessageMiddleware(lambda r: None).process_request(request)
        
        queryset = Booking.objects.filter(id=self.booking.id)
        self.admin.cancel_bookings(request, queryset)
        
        # Refresh booking from database
        self.booking.refresh_from_db()
        self.assertTrue(self.booking.is_cancelled)

    def test_room_queryset_filtering(self):
        """Test that room choices are filtered by room_category"""
        request = MockRequest()
        request.user = MockSuperUser()
        
        # Add middleware
        SessionMiddleware(lambda r: None).process_request(request)
        MessageMiddleware(lambda r: None).process_request(request)
        
        form = self.admin.get_form(request)
        self.assertEqual(
            form.base_fields['room'].queryset.model,
            Room
        ) 