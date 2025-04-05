from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('booking__user__username', 'stripe_payment_intent')
