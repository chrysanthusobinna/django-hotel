from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'is_paid')
    list_filter = ('is_paid', 'check_in', 'check_out')
    search_fields = ('user__username', 'room__name')
