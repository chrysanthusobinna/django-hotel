from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('booking-summary/', views.booking_summary,
         name='booking_summary'),
    path('create-checkout-session/', views.create_checkout_session,
         name='create_checkout_session'),
    path('payment-success/', views.payment_success,
         name='payment_success'),
    path('payment-cancelled/', views.payment_cancelled,
         name='payment_cancelled'),
]
