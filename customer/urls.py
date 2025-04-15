from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('dashboard/', views.dashboard, name='customer_dashboard'),
    path('booking/<str:booking_number>/', views.booking_detail, name='booking_detail'),
]
