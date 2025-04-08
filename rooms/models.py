from django.db import models
from cloudinary.models import CloudinaryField

class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = CloudinaryField('image', blank=True, null=True)


    def __str__(self):
        return self.name

class RoomCategoryImage(models.Model):
    room_category = models.ForeignKey(RoomCategory, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.room_category.name}"
        

class Room(models.Model):
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
