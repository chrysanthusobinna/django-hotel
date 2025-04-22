# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from ..models import UserProfile

# class ViewProfileViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
#         self.other_user = User.objects.create_user(
#             username='otheruser',
#             email='other@example.com',
#             password='testpass123'
#         )
#         self.staff_user = User.objects.create_user(
#             username='staffuser',
#             email='staff@example.com',
#             password='testpass123',
#             is_staff=True
#         )
#         self.profile = UserProfile.objects.create(
#             user=self.user,
#             address='123 Test St',
#             city='Test City',
#             post_code='12345',
#             country='Test Country'
#         )

#     def test_view_profile_authenticated_own_profile(self):
#         """Test that a user can view their own profile"""
#         self.client.login(username='testuser', password='testpass123')
#         response = self.client.get(reverse('profiles:view_profile', args=[self.user.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'testuser')
#         self.assertContains(response, '123 Test St')

#     def test_view_profile_authenticated_other_profile(self):
#         """Test that a user cannot view another user's profile"""
#         self.client.login(username='testuser', password='testpass123')
#         response = self.client.get(reverse('profiles:view_profile', args=[self.other_user.id]))
#         self.assertEqual(response.status_code, 302)  # Redirect to home
#         self.assertRedirects(response, reverse('mainsite:home'))

#     def test_view_profile_staff_access(self):
#         """Test that staff can view any profile"""
#         self.client.login(username='staffuser', password='testpass123')
#         response = self.client.get(reverse('profiles:view_profile', args=[self.user.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'testuser')

#     def test_view_profile_unauthenticated(self):
#         """Test that unauthenticated users cannot view profiles"""
#         response = self.client.get(reverse('profiles:view_profile', args=[self.user.id]))
#         self.assertEqual(response.status_code, 302)  # Redirect to login
#         self.assertRedirects(response, f'/accounts/login/?next=/profiles/profile/{self.user.id}/')

#     def test_view_profile_nonexistent_user(self):
#         """Test viewing a profile for a nonexistent user"""
#         self.client.login(username='testuser', password='testpass123')
#         response = self.client.get(reverse('profiles:view_profile', args=[999]))
#         self.assertEqual(response.status_code, 404) 