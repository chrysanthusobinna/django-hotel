from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rooms.models import RoomCategory, Room
from custom_admin.forms import RoomCategoryForm
from django.core.files.uploadedfile import SimpleUploadedFile

class RoomCategoryViewTest(TestCase):
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
        
        # Create test image
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )

    def test_room_category_list_requires_login(self):
        """Test that room category list requires login"""
        response = self.client.get(reverse('custom_admin:room_categories'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:room_categories')}")

    def test_room_category_list_requires_staff(self):
        """Test that room category list requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:room_categories'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('mainsite:home')}?next={reverse('custom_admin:room_categories')}")

    def test_room_category_list_accessible_by_staff(self):
        """Test that room category list is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:room_categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/room_categories.html')
        self.assertIn('categories', response.context)
        self.assertEqual(len(response.context['categories']), 1)

    def test_room_category_detail_requires_login(self):
        """Test that room category detail requires login"""
        response = self.client.get(reverse('custom_admin:room_category_detail', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:room_category_detail', args=[self.room_category.id])}")

    def test_room_category_detail_requires_staff(self):
        """Test that room category detail requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:room_category_detail', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('mainsite:home')}?next={reverse('custom_admin:room_category_detail', args=[self.room_category.id])}")

    def test_room_category_detail_accessible_by_staff(self):
        """Test that room category detail is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:room_category_detail', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/room_category_detail.html')
        self.assertIn('category', response.context)
        self.assertEqual(response.context['category'], self.room_category)
        self.assertIn('rooms', response.context)
        self.assertEqual(len(response.context['rooms']), 1)

    def test_room_category_create_requires_login(self):
        """Test that room category create requires login"""
        response = self.client.get(reverse('custom_admin:add_room_category'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:add_room_category')}")

    def test_room_category_create_requires_staff(self):
        """Test that room category create requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:add_room_category'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('mainsite:home')}?next={reverse('custom_admin:add_room_category')}")

    def test_room_category_create_accessible_by_staff(self):
        """Test that room category create is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:add_room_category'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/add_room_category.html')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], RoomCategoryForm)

    def test_room_category_create_valid_data(self):
        """Test creating a room category with valid data"""
        self.client.login(username='admin', password='adminpass123')
        form_data = {
            'name': 'New Category',
            'description': 'New Description',
            'price': 150.00,
        }
        response = self.client.post(reverse('custom_admin:add_room_category'), 
                                  data=form_data,
                                  files={'image': self.test_image})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(RoomCategory.objects.filter(name='New Category').exists())

    def test_room_category_update_requires_login(self):
        """Test that room category update requires login"""
        response = self.client.get(reverse('custom_admin:edit_room_category', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:edit_room_category', args=[self.room_category.id])}")

    def test_room_category_update_requires_staff(self):
        """Test that room category update requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('custom_admin:edit_room_category', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('mainsite:home')}?next={reverse('custom_admin:edit_room_category', args=[self.room_category.id])}")

    def test_room_category_update_accessible_by_staff(self):
        """Test that room category update is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('custom_admin:edit_room_category', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'custom_admin/edit_room_category.html')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], RoomCategoryForm)
        self.assertIn('category', response.context)
        self.assertEqual(response.context['category'], self.room_category)

    def test_room_category_update_valid_data(self):
        """Test updating a room category with valid data"""
        self.client.login(username='admin', password='adminpass123')
        form_data = {
            'name': 'Updated Category',
            'description': 'Updated Description',
            'price': 200.00,
        }
        response = self.client.post(reverse('custom_admin:edit_room_category', args=[self.room_category.id]), 
                                  data=form_data,
                                  files={'image': self.test_image})
        self.assertEqual(response.status_code, 302)
        updated_category = RoomCategory.objects.get(id=self.room_category.id)
        self.assertEqual(updated_category.name, 'Updated Category')
        self.assertEqual(updated_category.description, 'Updated Description')
        self.assertEqual(updated_category.price, 200.00)

    def test_room_category_delete_requires_login(self):
        """Test that room category delete requires login"""
        response = self.client.post(reverse('custom_admin:delete_roomcategory', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('custom_admin:delete_roomcategory', args=[self.room_category.id])}")

    def test_room_category_delete_requires_staff(self):
        """Test that room category delete requires staff status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('custom_admin:delete_roomcategory', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('mainsite:home')}?next={reverse('custom_admin:delete_roomcategory', args=[self.room_category.id])}")

    def test_room_category_delete_accessible_by_staff(self):
        """Test that room category delete is accessible by staff"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.post(reverse('custom_admin:delete_roomcategory', args=[self.room_category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(RoomCategory.objects.filter(id=self.room_category.id).exists()) 