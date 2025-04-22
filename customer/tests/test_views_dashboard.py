from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from bookings.models import Booking, RoomCategory
from datetime import datetime, timedelta

class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.url = reverse('customer:customer_dashboard')
        
        # Create a room category first
        self.room_category = RoomCategory.objects.create(
            name='Test Room',
            description='Test Description',
            price=100.00
        )
        
        # Create some test bookings with explicit creation times
        now = datetime.now()
        self.booking1 = Booking.objects.create(
            user=self.user,
            booking_number='TEST01',
            is_paid=True,
            check_in=now.date() + timedelta(days=1),
            check_out=now.date() + timedelta(days=3),
            room_category=self.room_category,
            created_at=now - timedelta(days=1)  # Older booking
        )
        self.booking2 = Booking.objects.create(
            user=self.user,
            booking_number='TEST02',
            is_paid=True,
            check_in=now.date() + timedelta(days=2),
            check_out=now.date() + timedelta(days=4),
            room_category=self.room_category,
            created_at=now  # Newer booking
        )

    def test_dashboard_requires_login(self):
        """
        Test that dashboard view requires login
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_dashboard_shows_bookings(self):
        """
        Test that dashboard shows user's bookings
        """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/dashboard.html')
        
        # Check if bookings are in context
        self.assertIn('bookings', response.context)
        self.assertEqual(len(response.context['bookings']), 2)
