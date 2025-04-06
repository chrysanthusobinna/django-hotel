from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Profile"
