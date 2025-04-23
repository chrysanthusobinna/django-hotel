from django.db import models
from django.utils import timezone

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_subscribed']

    def __str__(self):
        return self.email
