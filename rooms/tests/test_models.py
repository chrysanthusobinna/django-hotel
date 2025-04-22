from django.test import TestCase
from ..models import RoomCategory, RoomCategoryImage, Room

class RoomCategoryModelTest(TestCase):
    def setUp(self):
        self.room_category = RoomCategory.objects.create(
            name="Deluxe Suite",
            description="A luxurious suite with ocean view",
            price=299.99
        )

    def test_room_category_creation(self):
        self.assertEqual(self.room_category.name, "Deluxe Suite")
        self.assertEqual(self.room_category.price, 299.99)
        self.assertEqual(str(self.room_category), "Deluxe Suite")

class RoomCategoryImageModelTest(TestCase):
    def setUp(self):
        self.room_category = RoomCategory.objects.create(
            name="Deluxe Suite",
            description="A luxurious suite with ocean view",
            price=299.99
        )
        self.image = RoomCategoryImage.objects.create(
            room_category=self.room_category,
            caption="Ocean View"
        )

    def test_room_category_image_creation(self):
        self.assertEqual(self.image.room_category, self.room_category)
        self.assertEqual(self.image.caption, "Ocean View")
        self.assertEqual(str(self.image), f"Image for {self.room_category.name}")

class RoomModelTest(TestCase):
    def setUp(self):
        self.room_category = RoomCategory.objects.create(
            name="Deluxe Suite",
            description="A luxurious suite with ocean view",
            price=299.99
        )
        self.room = Room.objects.create(
            category=self.room_category,
            name="Room 101",
            is_available=True
        )

    def test_room_creation(self):
        self.assertEqual(self.room.name, "Room 101")
        self.assertEqual(self.room.category, self.room_category)
        self.assertTrue(self.room.is_available)
        self.assertEqual(str(self.room), "Room 101") 