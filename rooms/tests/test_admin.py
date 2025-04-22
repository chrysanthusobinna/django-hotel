from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import RoomCategory, Room

class RoomAdminTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpass123',
            email='admin@example.com'
        )
        self.client = Client()
        self.client.login(username='admin', password='adminpass123')

    def test_room_category_admin_list_display(self):
        RoomCategory.objects.create(
            name="Test Suite",
            description="Test description",
            price=199.99
        )
        response = self.client.get('/admin/rooms/roomcategory/')
        self.assertContains(response, "Test Suite")
        self.assertContains(response, "199.99")

    def test_room_admin_list_display(self):
        room_category = RoomCategory.objects.create(
            name="Test Suite",
            description="Test description",
            price=199.99
        )
        Room.objects.create(
            category=room_category,
            name="Test Room",
            is_available=True
        )
        response = self.client.get('/admin/rooms/room/')
        self.assertContains(response, "Test Room")
        self.assertContains(response, "Test Suite")
        self.assertContains(response, "Yes") 