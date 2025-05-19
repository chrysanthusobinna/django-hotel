from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from datetime import date, timedelta

class BookingListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create admin user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        
        # Create regular user
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
        
        # Create test bookings
        self.booking1 = Booking.objects.create(
            user=self.user,
            room_category=self.room_category,
            room=self.room,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            total_price=200.00
        )
        
        self.booking2 = Booking.objects.create(
            user=self.user,
            room_category=self.room_category,
            room=self.room,
            check_in=date.today() + timedelta(days=4),
            check_out=date.today() + timedelta(days=6),
            total_price=200.00,
            is_paid=True
        )

    def test_booking_list_requires_login(self):
        """Test that booking list requires login"""
        response = self.client.get(reverse('custom_admin:booking_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login'))

    def test_booking_list_requires_staff(self):
        """Test that booking list requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:booking_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_booking_list_accessible_by_staff(self):
        """Test that booking list is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/booking_list.html')

