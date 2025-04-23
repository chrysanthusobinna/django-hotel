from django.test import TestCase
from django.utils import timezone
from newsletter.models import Subscriber

class SubscriberModelTest(TestCase):
    def setUp(self):
        self.subscriber = Subscriber.objects.create(
            email='test@example.com'
        )

    def test_subscriber_creation(self):
        """Test that a subscriber can be created"""
        self.assertEqual(self.subscriber.email, 'test@example.com')
        self.assertTrue(self.subscriber.is_active)
        self.assertIsNotNone(self.subscriber.date_subscribed)

    def test_subscriber_str_representation(self):
        """Test the string representation of a subscriber"""
        self.assertEqual(str(self.subscriber), 'test@example.com')

    def test_subscriber_ordering(self):
        """Test that subscribers are ordered by date_subscribed in descending order"""
        Subscriber.objects.create(email='test2@example.com')
        subscribers = Subscriber.objects.all()
        self.assertEqual(subscribers[0].email, 'test2@example.com')
        self.assertEqual(subscribers[1].email, 'test@example.com')

    def test_subscriber_unique_email(self):
        """Test that email addresses must be unique"""
        with self.assertRaises(Exception):
            Subscriber.objects.create(email='test@example.com') 