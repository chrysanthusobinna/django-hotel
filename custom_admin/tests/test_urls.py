from django.test import TestCase
from django.urls import resolve, reverse

class CustomAdminUrlsTest(TestCase):
    def test_dashboard_url(self):
        """Test dashboard URL resolution"""
        url = reverse('custom_admin:dashboard')
        self.assertEqual(resolve(url).func.__name__, 'dashboard')

    def test_booking_list_url(self):
        """Test booking list URL resolution"""
        url = reverse('custom_admin:booking_list')
        self.assertEqual(resolve(url).func.__name__, 'booking_list')

    def test_booking_detail_url(self):
        """Test booking detail URL resolution"""
        url = reverse('custom_admin:booking_detail', args=[1])
        self.assertEqual(resolve(url).func.__name__, 'booking_detail')

    def test_update_checkin_url(self):
        """Test update checkin URL resolution"""
        url = reverse('custom_admin:update_checkin')
        self.assertEqual(resolve(url).func.__name__, 'update_checkin')

    def test_update_checkout_url(self):
        """Test update checkout URL resolution"""
        url = reverse('custom_admin:update_checkout')
        self.assertEqual(resolve(url).func.__name__, 'update_checkout')

    def test_cancel_booking_url(self):
        """Test cancel booking URL resolution"""
        url = reverse('custom_admin:cancel_booking')
        self.assertEqual(resolve(url).func.__name__, 'cancel_booking')

    def test_delete_booking_url(self):
        """Test delete booking URL resolution"""
        url = reverse('custom_admin:delete_booking')
        self.assertEqual(resolve(url).func.__name__, 'delete_booking') 