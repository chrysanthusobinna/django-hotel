from django.test import TestCase
from django.urls import reverse

class RoomURLsTest(TestCase):
    def test_room_list_url(self):
        url = reverse('rooms:room_list')
        self.assertEqual(url, '/room-categories/')

    def test_room_detail_url(self):
        url = reverse('rooms:room_detail', args=[1])
        self.assertEqual(url, '/room-details/1/') 