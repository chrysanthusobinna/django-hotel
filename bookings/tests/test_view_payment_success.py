from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from datetime import date, timedelta
from django.conf import settings

class PaymentSuccessViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com',
            first_name='Test',
            last_name='User'
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
        
        # Set up session data
        self.session_data = {
            'booking_id': self.booking.id,
            'booking_number': self.booking.booking_number,
            'room_category_id': self.room_category.id
        }
        
        # Login the user
        self.client.login(username='testuser', password='testpass123')

    def _set_session_data(self):
        """Helper method to set session data"""
        session = self.client.session
        session['booking'] = self.session_data
        session.save()

    def test_payment_success_without_session_data(self):
        """Test payment success redirects to home without session data"""
        response = self.client.get(reverse('bookings:payment_success'))
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_payment_success_with_invalid_booking_id(self):
        """Test payment success redirects to home with invalid booking ID"""
        self.session_data['booking_id'] = 99999  # Invalid ID
        self._set_session_data()
        
        response = self.client.get(reverse('bookings:payment_success'))
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_payment_success_updates_booking_status(self):
        """Test that payment success updates booking payment status"""
        self._set_session_data()
        
        response = self.client.get(reverse('bookings:payment_success'))
        
        # Refresh booking from database
        self.booking.refresh_from_db()
        self.assertTrue(self.booking.is_paid)

    def test_payment_success_already_paid_booking(self):
        """Test that already paid booking is handled correctly"""
        # Mark booking as paid
        self.booking.is_paid = True
        self.booking.save()
        
        self._set_session_data()
        response = self.client.get(reverse('bookings:payment_success'))
        
        # Check that no new email was sent
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(response.status_code, 200)

    def test_payment_success_sends_confirmation_email(self):
        """Test that payment success sends confirmation email"""
        self._set_session_data()
        
        response = self.client.get(reverse('bookings:payment_success'))
        
        # Check that email was sent
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, f"Booking Confirmation - #{self.booking.booking_number}")
        self.assertEqual(email.to, [self.user.email])
        self.assertEqual(email.from_email, settings.DEFAULT_FROM_EMAIL)

    def test_payment_success_email_content(self):
        """Test that payment success email contains correct information"""
        self._set_session_data()
        
        response = self.client.get(reverse('bookings:payment_success'))
        
        # Check email content
        email = mail.outbox[0]
        email_body = email.body
        
        # Check all required information is present
        self.assertIn(str(self.booking.booking_number), email_body)
        self.assertIn(self.room_category.name, email_body)
        self.assertIn(str(self.booking.check_in), email_body)
        self.assertIn(str(self.booking.check_out), email_body)
        self.assertIn(str(self.booking.total_price), email_body)
        self.assertIn(self.user.first_name, email_body)
        
        # Check email structure
        self.assertIn('Hi Test,', email_body)
        self.assertIn('Thank you for your booking!', email_body)
        self.assertIn('Booking Details:', email_body)
        self.assertIn('We look forward to your stay!', email_body)

    def test_payment_success_renders_template(self):
        """Test that payment success renders correct template with context"""
        self._set_session_data()
        
        response = self.client.get(reverse('bookings:payment_success'))
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/payment_success.html')
        
        # Check context data
        self.assertEqual(response.context['booking'], self.booking)
        self.assertEqual(response.context['room_category'], self.room_category) 