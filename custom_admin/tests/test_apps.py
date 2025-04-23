from django.test import TestCase
from django.apps import apps

class CustomAdminAppConfigTest(TestCase):
    def test_app_config(self):
        """Test that the app is configured correctly"""
        app_config = apps.get_app_config('custom_admin')
        self.assertEqual(app_config.name, 'custom_admin')
        self.assertEqual(app_config.verbose_name, 'Custom Admin') 