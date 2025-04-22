from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import UserProfile
from ..forms import UserForm, UserProfileForm

class EditProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.staff_user = User.objects.create_user(
            username='staffuser',
            email='staff@example.com',
            password='testpass123',
            is_staff=True
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            address='123 Test St',
            city='Test City',
            post_code='12345',
            country='Test Country'
        )

    def test_edit_profile_authenticated_get(self):
        """Test accessing edit profile page when authenticated"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profiles:edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')
        self.assertIsInstance(response.context['user_form'], UserForm)
        self.assertIsInstance(response.context['profile_form'], UserProfileForm)

    def test_edit_profile_unauthenticated(self):
        """Test accessing edit profile page when not authenticated"""
        response = self.client.get(reverse('profiles:edit_profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertRedirects(response, f'/accounts/login/?next=/profile/edit/')

    def test_edit_profile_valid_post(self):
        """Test submitting valid profile edit form"""
        self.client.login(username='testuser', password='testpass123')
        form_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'email': 'updated@example.com',
            'address': '456 New St',
            'city': 'New City',
            'post_code': '54321',
            'country': 'New Country'
        }
        response = self.client.post(reverse('profiles:edit_profile'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect to view profile
        self.assertRedirects(response, reverse('profiles:view_profile', args=[self.user.id]))

        # Verify updates
        self.user.refresh_from_db()
        self.profile.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'Name')
        self.assertEqual(self.user.email, 'updated@example.com')
        self.assertEqual(self.profile.address, '456 New St')
        self.assertEqual(self.profile.city, 'New City')
        self.assertEqual(self.profile.post_code, '54321')
        self.assertEqual(self.profile.country, 'New Country')

    def test_edit_profile_invalid_post(self):
        """Test submitting invalid profile edit form"""
        self.client.login(username='testuser', password='testpass123')
        form_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'email': 'invalid-email',
            'address': '456 New St',
            'city': 'New City',
            'post_code': '54321',
            'country': 'New Country'
        }
        response = self.client.post(reverse('profiles:edit_profile'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Form errors, stay on same page
        self.assertFormError(response.context['user_form'], 'email', 'Enter a valid email address.')


    def test_edit_profile_staff_access(self):
        """Test staff user accessing edit profile"""
        self.client.login(username='staffuser', password='testpass123')
        response = self.client.get(reverse('profiles:edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')
        self.assertIsInstance(response.context['user_form'], UserForm)
        self.assertIsNone(response.context['profile_form'])