from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import RoomCategory
from profiles.models import UserProfile

class RoomDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.room_category = RoomCategory.objects.create(
            name="Deluxe Suite",
            description="A luxurious suite with ocean view",
            price=299.99
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            address="123 Test St",
            city="Test City",
            post_code="12345",
            country="Test Country"
        )

    def test_room_detail_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('rooms:room_detail', args=[self.room_category.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/room_detail.html')
        self.assertContains(response, "Deluxe Suite")
        self.assertTrue(response.context['can_book'])
        self.assertFalse(response.context['incomplete_profile'])

    def test_room_detail_view_unauthenticated(self):
        response = self.client.get(reverse('rooms:room_detail', args=[self.room_category.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['can_book'])

    def test_room_detail_view_incomplete_profile(self):
        self.profile.address = ""
        self.profile.save()
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('rooms:room_detail', args=[self.room_category.pk]))
        self.assertTrue(response.context['incomplete_profile']) 