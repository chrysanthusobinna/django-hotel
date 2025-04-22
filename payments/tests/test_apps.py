from django.test import TestCase
from payments.apps import PaymentsConfig

class PaymentsConfigTest(TestCase):
    def test_app_config(self):
        """Test the PaymentsConfig configuration"""
        self.assertEqual(PaymentsConfig.name, 'payments')
        self.assertEqual(PaymentsConfig.default_auto_field, 'django.db.models.BigAutoField') 