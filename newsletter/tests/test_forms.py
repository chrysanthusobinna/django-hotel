from django.test import TestCase
from newsletter.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_form_valid_data(self):
        """Test form with valid data"""
        form_data = {'email': 'test@example.com'}
        form = SubscriptionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """Test form with invalid data"""
        form_data = {'email': 'invalid-email'}
        form = SubscriptionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_empty_data(self):
        """Test form with empty data"""
        form = SubscriptionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_widget_attributes(self):
        """Test form widget attributes"""
        form = SubscriptionForm()
        email_field = form.fields['email']
        self.assertEqual(email_field.widget.attrs['class'], 'form-control')
        self.assertEqual(email_field.widget.attrs['placeholder'], 'Enter your email address')
        self.assertTrue(email_field.widget.attrs['required']) 