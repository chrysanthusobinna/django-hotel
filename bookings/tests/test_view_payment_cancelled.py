from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class PaymentCancelledViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('bookings:payment_cancelled')

    def test_payment_cancelled_renders_template(self):
        """Test that payment cancelled view renders correct template"""
        response = self.client.get(self.url)
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/payment_cancelled.html')
        
        # Check context
        self.assertIn('message', response.context)
        self.assertEqual(response.context['message'], 'Payment was cancelled. You can try again.')

    def test_payment_cancelled_anonymous_access(self):
        """Test that payment cancelled view is accessible to anonymous users"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        # Check messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Payment was cancelled. You can try again.')
        self.assertEqual(messages[0].level, 30)  # 30 is the level for WARNING

    def test_payment_cancelled_authenticated_access(self):
        """Test that payment cancelled view is accessible to authenticated users"""
        # Create and login a test user
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        # Check messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Payment was cancelled. You can try again.')
        self.assertEqual(messages[0].level, 30)  # 30 is the level for WARNING 