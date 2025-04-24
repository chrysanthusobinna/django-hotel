from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from datetime import date, timedelta
import stripe
from django.conf import settings

class CreateCheckoutSessionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
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
        
        # Set up test session data
        self.check_in = date.today() + timedelta(days=1)
        self.check_out = self.check_in + timedelta(days=2)
        self.session_data = {
            'room_category_id': self.room_category.id,
            'check_in': self.check_in.strftime('%Y-%m-%d'),
            'check_out': self.check_out.strftime('%Y-%m-%d'),
            'nights': 2,
            'total_price': 200.00
        }
        
        # Login the user
        self.client.login(username='testuser', password='testpass123')
        
        # Set up Stripe test key
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def test_create_checkout_session_without_session_data(self):
        """Test that checkout session redirects to home without session data"""
        response = self.client.get(reverse('bookings:create_checkout_session'))
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_create_checkout_session_with_valid_data(self):
        """Test checkout session creation with valid data"""
        # Set session data
        session = self.client.session
        session['booking'] = self.session_data
        session.save()
        
        response = self.client.get(reverse('bookings:create_checkout_session'))
        
        # Check that a booking was created
        self.assertTrue(Booking.objects.filter(user=self.user).exists())
        
        # Check that the booking has the correct data
        booking = Booking.objects.get(user=self.user)
        self.assertEqual(booking.room_category, self.room_category)
        self.assertEqual(booking.check_in, self.check_in)
        self.assertEqual(booking.check_out, self.check_out)
        self.assertEqual(booking.total_price, 200.00)
        self.assertFalse(booking.is_paid)

    def test_create_checkout_session_creates_booking(self):
        """Test that checkout session creates a booking with correct data"""
        # Set session data
        session = self.client.session
        session['booking'] = self.session_data
        session.save()
        
        response = self.client.get(reverse('bookings:create_checkout_session'))
        
        # Check booking creation
        booking = Booking.objects.get(user=self.user)
        self.assertIsNotNone(booking.booking_number)
        self.assertEqual(booking.total_price, 200.00)
        self.assertFalse(booking.is_paid)
        self.assertFalse(booking.is_cancelled)

    def test_create_checkout_session_updates_session(self):
        """Test that checkout session updates session data with booking info"""
        # Set session data
        session = self.client.session
        session['booking'] = self.session_data
        session.save()
        
        response = self.client.get(reverse('bookings:create_checkout_session'))
        
        # Check session data
        updated_session = self.client.session
        self.assertIn('booking', updated_session)
        self.assertIn('booking_id', updated_session['booking'])
        self.assertIn('booking_number', updated_session['booking']) 