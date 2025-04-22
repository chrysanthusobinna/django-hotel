# from django.test import TestCase
# from django.contrib.auth.models import User
# from ..models import UserProfile

# class UserProfileSignalsTest(TestCase):
#     def test_profile_creation_on_user_creation(self):
#         """Test that a UserProfile is automatically created when a User is created"""
#         # Create a new user
#         user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
        
#         # Check if a profile was created
#         self.assertTrue(UserProfile.objects.filter(user=user).exists())
        
#         # Get the created profile
#         profile = UserProfile.objects.get(user=user)
        
#         # Verify the profile is properly linked
#         self.assertEqual(profile.user, user)
        
#         # Verify default values
#         self.assertEqual(profile.address, '')
#         self.assertEqual(profile.city, '')
#         self.assertEqual(profile.post_code, '')
#         self.assertEqual(profile.country, '')

#     def test_profile_not_created_on_user_update(self):
#         """Test that a new profile is not created when an existing user is updated"""
#         # Create a user
#         user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
        
#         # Count initial profiles
#         initial_profile_count = UserProfile.objects.count()
        
#         # Update the user
#         user.first_name = 'Updated'
#         user.save()
        
#         # Verify no new profile was created
#         self.assertEqual(UserProfile.objects.count(), initial_profile_count) 