# from django.test import TestCase
# from django.contrib.auth.models import User
# from ..forms import CustomSignupForm, UserForm, UserProfileForm
# from ..models import UserProfile

# class CustomSignupFormTest(TestCase):
#     def test_custom_signup_form_valid_data(self):
#         form_data = {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password1': 'testpass123',
#             'password2': 'testpass123',
#             'first_name': 'Test',
#             'last_name': 'User',
#             'middle_name': 'Middle'
#         }
#         form = CustomSignupForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_custom_signup_form_save(self):
#         form_data = {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password1': 'testpass123',
#             'password2': 'testpass123',
#             'first_name': 'Test',
#             'last_name': 'User',
#             'middle_name': 'Middle'
#         }
#         form = CustomSignupForm(data=form_data)
#         if form.is_valid():
#             user = form.save(None)
#             self.assertEqual(user.first_name, 'Test')
#             self.assertEqual(user.last_name, 'User')

# class UserFormTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )

#     def test_user_form_valid_data(self):
#         form_data = {
#             'first_name': 'Updated',
#             'last_name': 'Name',
#             'email': 'updated@example.com'
#         }
#         form = UserForm(data=form_data, instance=self.user)
#         self.assertTrue(form.is_valid())

#     def test_user_form_invalid_email(self):
#         form_data = {
#             'first_name': 'Test',
#             'last_name': 'User',
#             'email': 'invalid-email'
#         }
#         form = UserForm(data=form_data, instance=self.user)
#         self.assertFalse(form.is_valid())

# class UserProfileFormTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
#         self.profile = UserProfile.objects.create(
#             user=self.user,
#             address='123 Test St',
#             city='Test City',
#             post_code='12345',
#             country='Test Country'
#         )

#     def test_user_profile_form_valid_data(self):
#         form_data = {
#             'address': '456 New St',
#             'city': 'New City',
#             'post_code': '54321',
#             'country': 'New Country'
#         }
#         form = UserProfileForm(data=form_data, instance=self.profile)
#         self.assertTrue(form.is_valid())

#     def test_user_profile_form_required_fields(self):
#         form_data = {
#             'address': '',
#             'city': '',
#             'post_code': '',
#             'country': ''
#         }
#         form = UserProfileForm(data=form_data, instance=self.profile)
#         self.assertFalse(form.is_valid()) 