from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('summary/', views.booking_summary, name='booking_summary'),
]


# ==

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('booking-summary/', views.booking_summary, name='booking_summary'),
# ]
