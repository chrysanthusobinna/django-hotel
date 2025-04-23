from django.test import TestCase, Client
from django.urls import reverse
from newsletter.models import Subscriber
from django.contrib import messages

class NewsletterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.subscribe_url = reverse('newsletter:subscribe_newsletter')

    def test_subscribe_new_email(self):
        """Test subscribing with a new email address"""
        response = self.client.post(self.subscribe_url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(Subscriber.objects.filter(email='test@example.com').exists())
        # Check if success message is set
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), 'Thank you for subscribing to our newsletter!')

    def test_subscribe_existing_email(self):
        """Test subscribing with an existing email address"""
        # Create a subscriber first
        Subscriber.objects.create(email='test@example.com')
        
        # Try to subscribe with the same email
        response = self.client.post(self.subscribe_url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)  # Redirect
        
        # Check if info message is set
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), 'You are already subscribed to our newsletter!')

    def test_subscribe_invalid_email(self):
        """Test subscribing with an invalid email address"""
        response = self.client.post(self.subscribe_url, {'email': 'invalid-email'})
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertFalse(Subscriber.objects.filter(email='invalid-email').exists())

    def test_subscribe_get_request(self):
        """Test GET request to subscribe endpoint"""
        response = self.client.get(self.subscribe_url)
        self.assertEqual(response.status_code, 302)  # Redirect 