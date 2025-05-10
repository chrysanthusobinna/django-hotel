from django.contrib import admin
from django import forms
from .models import Booking, Room


# Custom form to filter rooms by room_category
class BookingAdminForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Restrict room choices based on room_category
        if self.instance and self.instance.room_category:
            self.fields['room'].queryset = Room.objects.filter(
                category=self.instance.room_category
            )
        else:
            self.fields['room'].queryset = Room.objects.none()


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    form = BookingAdminForm

    list_display = (
        'booking_number',
        'user',
        'room_category',
        'room',
        'check_in',
        'check_out',
        'is_paid',
        'is_cancelled',
        'created_at',
    )
    list_filter = (
        'is_paid',
        'is_cancelled',
        'check_in',
        'check_out',
        'room_category'
    )
    search_fields = (
        'booking_number',
        'user__username',
        'room__name',
        'room_category__name'
    )
    ordering = ('-created_at',)
    readonly_fields = ('booking_number', 'created_at')
    actions = ['cancel_bookings']

    fieldsets = (
        (None, {
            'fields': ('booking_number', 'user', 'room_category', 'room')
        }),
        ('Dates', {
            'fields': (
                'check_in',
                'check_out',
                'actual_check_in',
                'actual_check_out'
            )
        }),
        ('Payment & Status', {
            'fields': (
                'is_paid',
                'is_cancelled',
                'total_price',
                'created_at'
            )
        }),
    )

    def cancel_bookings(self, request, queryset):
        updated = queryset.update(is_cancelled=True)
        self.message_user(
            request,
            f'Successfully cancelled {updated} booking(s).'
        )
    cancel_bookings.short_description = 'Cancel selected bookings'
