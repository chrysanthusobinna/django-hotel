from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from newsletter.models import Subscriber

class SubscriberAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.client.login(username='admin', password='adminpass123')
        self.subscriber = Subscriber.objects.create(
            email='test@example.com'
        )

    def test_subscriber_list_display(self):
        """Test that the subscriber list displays the correct fields"""
        url = reverse('admin:newsletter_subscriber_changelist')
        response = self.client.get(url)
        self.assertContains(response, 'test@example.com')
        self.assertContains(response, 'date_subscribed')
        self.assertContains(response, 'is_active')

    def test_subscriber_search(self):
        """Test that the subscriber search works"""
        url = reverse('admin:newsletter_subscriber_changelist')
        response = self.client.get(url, {'q': 'test@example.com'})
        self.assertContains(response, 'test@example.com')

    def test_subscriber_filter(self):
        """Test that the subscriber filters work"""
        url = reverse('admin:newsletter_subscriber_changelist')
        response = self.client.get(url, {'is_active__exact': '1'})
        self.assertContains(response, 'test@example.com') 