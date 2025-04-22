from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from bookings.models import Booking, RoomCategory
from datetime import datetime, date, timedelta

class BookingDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        
        # Create a room category first
        self.room_category = RoomCategory.objects.create(
            name='Test Room',
            description='Test Description',
            price=100.00
        )
        
        # Create a test booking with required fields
        self.booking = Booking.objects.create(
            user=self.user,
            booking_number='TEST01', 
            is_paid=True,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            room_category=self.room_category,  
            created_at=datetime.now()
        )

    def test_booking_detail_requires_login(self):
        """
        Test that booking detail view requires login
        """
        url = reverse('customer:booking_detail', kwargs={'booking_number': self.booking.booking_number})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_booking_detail_shows_correct_booking(self):
        """
        Test that booking detail shows the correct booking
        """
        self.client.login(username='testuser', password='testpass123')
        url = reverse('customer:booking_detail', kwargs={'booking_number': self.booking.booking_number})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/booking_detail.html')
        self.assertEqual(response.context['booking'], self.booking)
        self.assertEqual(response.context['today'], date.today())

    def test_cannot_view_other_users_booking(self):
        """
        Test that users cannot view other users' bookings
        """
        self.client.login(username='otheruser', password='testpass123')
        url = reverse('customer:booking_detail', kwargs={'booking_number': self.booking.booking_number})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 404)  # Should return 404 for other user's booking 