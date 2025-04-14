import random
import string
from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room, RoomCategory

def generate_booking_number():
    return ''.join(random.choices(string.digits, k=6))

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    booking_number = models.CharField(max_length=6, unique=True, editable=False, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not self.booking_number:
            while True:
                new_number = generate_booking_number()
                if not Booking.objects.filter(booking_number=new_number).exists():
                    self.booking_number = new_number
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.booking_number} ({self.check_in} to {self.check_out})"
