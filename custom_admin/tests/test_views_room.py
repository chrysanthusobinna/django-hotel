from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rooms.models import RoomCategory, Room

class RoomViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create admin user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        
        # Create regular user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create test room category
        self.room_category = RoomCategory.objects.create(
            name='Test Category',
            description='Test Description',
            price=100.00
        )
        
        # Create test room
        self.room = Room.objects.create(
            name='Test Room',
            category=self.room_category,
            is_available=True
        )

    def test_room_create_requires_login(self):
        """Test that room create requires login"""
        response = self.client.get(reverse('custom_admin:add_room'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login'))

    def test_room_create_requires_staff(self):
        """Test that room create requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:add_room'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_room_create_accessible_by_staff(self):
        """Test that room create is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:add_room'))
        self.assertEqual(response.status_code, 302)  # Redirects to room categories list

    def test_room_create_valid_data(self):
        """Test creating a room with valid data"""
        self.client.login(username='admin', password='adminpass123')
        form_data = {
            'category': self.room_category.id,
            'name': 'New Room',
            'is_available': 'on'
        }
        response = self.client.post(reverse('custom_admin:add_room'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Room.objects.filter(name='New Room').exists())

    def test_room_update_requires_login(self):
        """Test that room update requires login"""
        response = self.client.get(reverse('custom_admin:edit_room', args=[self.room.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login'))

    def test_room_update_requires_staff(self):
        """Test that room update requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:edit_room', args=[self.room.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_room_update_accessible_by_staff(self):
        """Test that room update is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:edit_room', args=[self.room.id]))
        self.assertEqual(response.status_code, 302)  # Redirects to room category detail

    def test_room_update_valid_data(self):
        """Test updating a room with valid data"""
        self.client.login(username='admin', password='adminpass123')
        form_data = {
            'name': 'Updated Room',
            'is_available': 'on'
        }
        response = self.client.post(reverse('custom_admin:edit_room', args=[self.room.id]), data=form_data)
        self.assertEqual(response.status_code, 302)
        updated_room = Room.objects.get(id=self.room.id)
        self.assertEqual(updated_room.name, 'Updated Room')
        self.assertTrue(updated_room.is_available)

    def test_room_delete_requires_login(self):
        """Test that room delete requires login"""
        response = self.client.post(reverse('custom_admin:delete_room', args=[self.room.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login'))

    def test_room_delete_requires_staff(self):
        """Test that room delete requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('custom_admin:delete_room', args=[self.room.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('mainsite:home'))

    def test_room_delete_accessible_by_staff(self):
        """Test that room delete is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.post(reverse('custom_admin:delete_room', args=[self.room.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Room.objects.filter(id=self.room.id).exists()) 