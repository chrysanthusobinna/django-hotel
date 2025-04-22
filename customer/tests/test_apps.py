from django.test import TestCase
from django.apps import apps
from customer.apps import CustomerConfig

class CustomerConfigTest(TestCase):
    def test_app_config(self):
        """
        Test if the CustomerConfig is properly configured
        """
        # Get the app config from the registry instead of creating it manually
        app_config = apps.get_app_config('customer')
        
        # Test that it's the correct class
        self.assertIsInstance(app_config, CustomerConfig)
        
        # Test default_auto_field
        self.assertEqual(app_config.default_auto_field, 'django.db.models.BigAutoField')
        
        # Test app name
        self.assertEqual(app_config.name, 'customer') 