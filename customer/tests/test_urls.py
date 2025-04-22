from django.test import TestCase
from django.urls import resolve, reverse
from customer import views

class CustomerUrlsTest(TestCase):
    def test_dashboard_url(self):
        """
        Test if the dashboard URL is properly configured
        """
        url = reverse('customer:customer_dashboard')
        self.assertEqual(url, '/customer/dashboard/')
        self.assertEqual(resolve(url).func, views.dashboard)

    def test_booking_detail_url(self):
        """
        Test if the booking detail URL is properly configured
        """
        url = reverse('customer:booking_detail', kwargs={'booking_number': 'TEST123'})
        self.assertEqual(url, '/customer/booking/TEST123/')
        self.assertEqual(resolve(url).func, views.booking_detail) 