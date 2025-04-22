from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from bookings.models import Booking, Room, RoomCategory
from payments.models import Payment
from django.contrib.auth.models import User

class PaymentAdminTest(TestCase):
    def setUp(self):
        # Create admin user
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.client = Client()
        self.client.login(username='admin', password='adminpass123')
        
        # Create a test user
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create a room category
        self.room_category = RoomCategory.objects.create(
            name='Deluxe',
            description='Deluxe room category',
            price=100.00
        )
        
        # Create a room
        self.room = Room.objects.create(
            name='Room 101',
            category=self.room_category,
            is_available=True
        )
        
        # Create a test booking
        self.booking = Booking.objects.create(
            user=self.test_user,
            room=self.room,
            room_category=self.room_category,
            check_in='2024-04-22',
            check_out='2024-04-24',
            total_price=200.00
        )
        
        # Create a test payment
        self.payment = Payment.objects.create(
            booking=self.booking,
            stripe_payment_intent='test_payment_intent_123',
            amount=200.00,
            status='completed'
        )

    def test_payment_list_display(self):
        """Test that the payment list displays the correct fields"""
        url = reverse('admin:payments_payment_changelist')
        response = self.client.get(url)
        
        self.assertContains(response, str(self.booking))
        self.assertContains(response, '200.00')
        self.assertContains(response, 'completed')

    def test_payment_search(self):
        """Test that the payment search works"""
        url = reverse('admin:payments_payment_changelist')
        response = self.client.get(url, {'q': 'test_payment_intent_123'})
        
        self.assertContains(response, str(self.payment))

    def test_payment_filter(self):
        """Test that the payment filter works"""
        url = reverse('admin:payments_payment_changelist')
        response = self.client.get(url, {'status': 'completed'})
        
        self.assertContains(response, str(self.payment))

    def test_payment_detail_view(self):
        """Test that the payment detail view shows all fields"""
        url = reverse('admin:payments_payment_change', args=[self.payment.id])
        response = self.client.get(url)
        
        self.assertContains(response, str(self.booking))
        self.assertContains(response, '200.00')
        self.assertContains(response, 'completed')
        self.assertContains(response, 'test_payment_intent_123') 