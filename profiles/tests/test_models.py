# from django.test import TestCase
# from django.contrib.auth.models import User
# from ..models import UserProfile

# class UserProfileModelTest(TestCase):
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

#     def test_user_profile_creation(self):
#         """Test that a UserProfile is created correctly"""
#         self.assertEqual(self.profile.user, self.user)
#         self.assertEqual(self.profile.address, '123 Test St')
#         self.assertEqual(self.profile.city, 'Test City')
#         self.assertEqual(self.profile.post_code, '12345')
#         self.assertEqual(self.profile.country, 'Test Country')

#     def test_user_profile_str_method(self):
#         """Test the __str__ method of UserProfile"""
#         expected_str = "testuser's Profile"
#         self.assertEqual(str(self.profile), expected_str)

#     def test_user_profile_one_to_one_relationship(self):
#         """Test the one-to-one relationship between User and UserProfile"""
#         self.assertEqual(self.user.profile, self.profile)
#         self.assertEqual(self.profile.user, self.user)

#     def test_user_profile_required_fields(self):
#         """Test that required fields cannot be empty"""
#         with self.assertRaises(Exception):
#             UserProfile.objects.create(
#                 user=self.user,
#                 address='',
#                 city='',
#                 post_code='',
#                 country=''
#             ) 