from django.test import TestCase, Client
from django.urls import reverse
from ..models import RoomCategory

class RoomListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.room_category = RoomCategory.objects.create(
            name="Deluxe Suite",
            description="A luxurious suite with ocean view",
            price=299.99
        )

    def test_room_list_view(self):
        response = self.client.get(reverse('rooms:room_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/room_list.html')
        self.assertContains(response, "Deluxe Suite") 