from django.test import TestCase
from django.urls import reverse, resolve
from newsletter.views import subscribe_newsletter

class NewsletterURLTest(TestCase):
    def test_subscribe_url(self):
        """Test that the subscribe URL resolves to the correct view"""
        url = reverse('newsletter:subscribe_newsletter')
        self.assertEqual(resolve(url).func, subscribe_newsletter) 