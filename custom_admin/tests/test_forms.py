from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rooms.models import RoomCategory, RoomCategoryImage
from custom_admin.forms import RoomCategoryForm, RoomCategoryImageForm

class RoomCategoryFormTest(TestCase):
    def setUp(self):
        # Create a test image file with actual content
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )

    def test_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'name': 'Test Category',
            'description': 'Test Description',
            'price': 100.00,
        }
        form = RoomCategoryForm(data=form_data, files={'image': self.test_image})
        self.assertTrue(form.is_valid())

    def test_form_invalid_price(self):
        """Test form validation with invalid price"""
        form_data = {
            'name': 'Test Category',
            'description': 'Test Description',
            'price': -1,
            'image': self.test_image
        }
        form = RoomCategoryForm(data=form_data, files={'image': self.test_image})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['price'][0], 'Price must be at least 1.')

    def test_form_missing_required_fields(self):
        """Test form with missing required fields"""
        form_data = {
            'name': 'Test Category',
            # Missing description and price
        }
        form = RoomCategoryForm(data=form_data, files={'image': self.test_image})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)
        self.assertIn('price', form.errors)

class RoomCategoryImageFormTest(TestCase):
    def setUp(self):
        # Create a test image file with actual content
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake-image-content',
            content_type='image/jpeg'
        )
        
        # Create a test room category
        self.room_category = RoomCategory.objects.create(
            name='Test Category',
            description='Test Description',
            price=100.00
        )

    def test_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'caption': 'Test Caption',
            'room_category': self.room_category.id
        }
        form = RoomCategoryImageForm(data=form_data, files={'image': self.test_image})
        self.assertTrue(form.is_valid())

    def test_form_without_caption(self):
        """Test form without caption (should be valid as caption is optional)"""
        form_data = {
            'room_category': self.room_category.id
        }
        form = RoomCategoryImageForm(data=form_data, files={'image': self.test_image})
        self.assertTrue(form.is_valid())

    def test_form_without_image(self):
        """Test form without image (should be invalid)"""
        form_data = {
            'caption': 'Test Caption',
            'room_category': self.room_category.id
        }
        form = RoomCategoryImageForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors) 