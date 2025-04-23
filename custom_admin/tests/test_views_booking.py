from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rooms.models import RoomCategory, Room
from bookings.models import Booking
from datetime import date, timedelta
from django.utils import timezone

class BookingViewTest(TestCase):
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
        
        # Create test booking
        self.booking = Booking.objects.create(
            user=self.user,
            room_category=self.room_category,
            room=self.room,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            total_price=200.00
        )

    def test_booking_list_requires_login(self):
        """Test that booking list requires login"""
        response = self.client.get(reverse('custom_admin:booking_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:booking_list')}")

    def test_booking_list_requires_staff(self):
        """Test that booking list requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:booking_list'))
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL starts with the home page URL
        self.assertTrue(response.url.startswith(reverse('mainsite:home')))
        # Check that the next parameter is present
        self.assertIn('next=', response.url)

    def test_booking_list_accessible_by_staff(self):
        """Test that booking list is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/booking_list.html')
        self.assertIn('bookings', response.context)
        self.assertEqual(len(response.context['bookings']), 1)

    def test_booking_detail_requires_login(self):
        """Test that booking detail requires login"""
        response = self.client.get(reverse('custom_admin:booking_detail', args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:booking_detail', args=[self.booking.id])}")

    def test_booking_detail_requires_staff(self):
        """Test that booking detail requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:booking_detail', args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL starts with the home page URL
        self.assertTrue(response.url.startswith(reverse('mainsite:home')))
        # Check that the next parameter is present
        self.assertIn('next=', response.url)

    def test_booking_detail_accessible_by_staff(self):
        """Test that booking detail is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:booking_detail', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/booking_detail.html')
        self.assertIn('booking', response.context)
        self.assertEqual(response.context['booking'], self.booking)
        self.assertIn('available_rooms', response.context)

    def test_booking_update_requires_login(self):
        """Test that booking update requires login"""
        response = self.client.post(reverse('custom_admin:update_checkin'), {
            'booking_id': self.booking.id,
            'check_in_datetime': timezone.now().strftime('%Y-%m-%dT%H:%M')
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:update_checkin')}")

    def test_booking_update_requires_staff(self):
        """Test that booking update requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('custom_admin:update_checkin'), {
            'booking_id': self.booking.id,
            'check_in_datetime': timezone.now().strftime('%Y-%m-%dT%H:%M')
        })
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL starts with the home page URL
        self.assertTrue(response.url.startswith(reverse('mainsite:home')))
        # Check that the next parameter is present
        self.assertIn('next=', response.url)

    def test_booking_update_valid_data(self):
        """Test updating a booking with valid data"""
        self.client.login(username='admin', password='adminpass123')
        check_in_datetime = timezone.now().strftime('%Y-%m-%dT%H:%M')
        response = self.client.post(reverse('custom_admin:update_checkin'), {
            'booking_id': self.booking.id,
            'check_in_datetime': check_in_datetime
        })
        self.assertEqual(response.status_code, 302)
        updated_booking = Booking.objects.get(id=self.booking.id)
        self.assertIsNotNone(updated_booking.actual_check_in)

    def test_booking_delete_requires_login(self):
        """Test that booking delete requires login"""
        response = self.client.post(reverse('custom_admin:delete_booking'), {
            'booking_id': self.booking.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:delete_booking')}")

    def test_booking_delete_requires_staff(self):
        """Test that booking delete requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('custom_admin:delete_booking'), {
            'booking_id': self.booking.id
        })
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL starts with the home page URL
        self.assertTrue(response.url.startswith(reverse('mainsite:home')))
        # Check that the next parameter is present
        self.assertIn('next=', response.url)

    def test_booking_delete_valid_data(self):
        """Test deleting a booking with valid data"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.post(reverse('custom_admin:delete_booking'), {
            'booking_id': self.booking.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())

    def test_booking_cancel_requires_login(self):
        """Test that booking cancel requires login"""
        response = self.client.post(reverse('custom_admin:cancel_booking'), {
            'booking_id': self.booking.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:cancel_booking')}")

    def test_booking_cancel_requires_staff(self):
        """Test that booking cancel requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('custom_admin:cancel_booking'), {
            'booking_id': self.booking.id
        })
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL starts with the home page URL
        self.assertTrue(response.url.startswith(reverse('mainsite:home')))
        # Check that the next parameter is present
        self.assertIn('next=', response.url)

    def test_booking_cancel_valid_data(self):
        """Test cancelling a booking with valid data"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.post(reverse('custom_admin:cancel_booking'), {
            'booking_id': self.booking.id
        })
        self.assertEqual(response.status_code, 302)
        updated_booking = Booking.objects.get(id=self.booking.id)
        self.assertTrue(updated_booking.is_cancelled)

    def test_room_assign_requires_login(self):
        """Test that room assign requires login"""
        response = self.client.post(reverse('custom_admin:assign_room'), {
            'booking_id': self.booking.id,
            'room_id': self.room.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:assign_room')}")

    def test_room_assign_requires_staff(self):
        """Test that room assign requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('custom_admin:assign_room'), {
            'booking_id': self.booking.id,
            'room_id': self.room.id
        })
        self.assertEqual(response.status_code, 302)
        # Check that the redirect URL starts with the home page URL
        self.assertTrue(response.url.startswith(reverse('mainsite:home')))
        # Check that the next parameter is present
        self.assertIn('next=', response.url)

    def test_room_assign_valid_data(self):
        """Test assigning a room with valid data"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.post(reverse('custom_admin:assign_room'), {
            'booking_id': self.booking.id,
            'room_id': self.room.id
        })
        self.assertEqual(response.status_code, 302)
        updated_booking = Booking.objects.get(id=self.booking.id)
        self.assertEqual(updated_booking.room, self.room) 