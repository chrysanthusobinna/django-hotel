# from django.test import TestCase
# from django.urls import reverse, resolve
# from ..views import view_profile, edit_profile

# class ProfilesURLTests(TestCase):
#     def test_view_profile_url_resolves(self):
#         """Test that the view_profile URL pattern resolves to the correct view"""
#         url = reverse('profiles:view_profile', args=[1])
#         self.assertEqual(resolve(url).func, view_profile)

#     def test_edit_profile_url_resolves(self):
#         """Test that the edit_profile URL pattern resolves to the correct view"""
#         url = reverse('profiles:edit_profile')
#         self.assertEqual(resolve(url).func, edit_profile)

#     def test_view_profile_url_pattern(self):
#         """Test that the view_profile URL pattern matches the expected format"""
#         url = reverse('profiles:view_profile', args=[1])
#         self.assertEqual(url, '/profiles/profile/1/')

#     def test_edit_profile_url_pattern(self):
#         """Test that the edit_profile URL pattern matches the expected format"""
#         url = reverse('profiles:edit_profile')
#         self.assertEqual(url, '/profiles/profile/edit/') 