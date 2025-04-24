from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from datetime import date, timedelta

class BookingSummaryViewTest(TestCase):
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
        
        # Login the user
        self.client.login(username='testuser', password='testpass123')

    def test_booking_summary_get_without_session(self):
        """Test that booking summary redirects to home without session data"""
        response = self.client.get(reverse('bookings:booking_summary'))
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_booking_summary_post_valid_data(self):
        """Test booking summary with valid POST data"""
        check_in = date.today() + timedelta(days=1)
        check_out = check_in + timedelta(days=2)
        
        response = self.client.post(reverse('bookings:booking_summary'), {
            'room_category_id': self.room_category.id,
            'check_in': check_in.strftime('%Y-%m-%d'),
            'check_out': check_out.strftime('%Y-%m-%d')
        })
        
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertIn('booking', self.client.session)

    def test_booking_summary_post_invalid_dates(self):
        """Test booking summary with invalid dates"""
        check_in = date.today() - timedelta(days=1)  # Past date
        
        response = self.client.post(reverse('bookings:booking_summary'), {
            'room_category_id': self.room_category.id,
            'check_in': check_in.strftime('%Y-%m-%d'),
            'check_out': date.today().strftime('%Y-%m-%d'),
            'adults': '2',
            'children': '1'
        })
        
        self.assertEqual(response.status_code, 302)  # Should redirect with error
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any('Check-in date cannot be in the past' in str(msg) for msg in messages))

    def test_booking_summary_post_same_dates(self):
        """Test booking summary with same check-in and check-out dates"""
        check_in = date.today() + timedelta(days=1)
        
        response = self.client.post(reverse('bookings:booking_summary'), {
            'room_category_id': self.room_category.id,
            'check_in': check_in.strftime('%Y-%m-%d'),
            'check_out': check_in.strftime('%Y-%m-%d')
        })
        
        self.assertEqual(response.status_code, 302)  # Should redirect with error
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any('Check-out date must be after check-in' in str(msg) for msg in messages))

    def test_booking_summary_post_checkout_before_checkin(self):
        """Test booking summary with check-out before check-in"""
        check_in = date.today() + timedelta(days=2)
        check_out = check_in - timedelta(days=1)
        
        response = self.client.post(reverse('bookings:booking_summary'), {
            'room_category_id': self.room_category.id,
            'check_in': check_in.strftime('%Y-%m-%d'),
            'check_out': check_out.strftime('%Y-%m-%d')
        })
        
        self.assertEqual(response.status_code, 302)  # Should redirect with error
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any('Check-out date must be after check-in' in str(msg) for msg in messages)) 