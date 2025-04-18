from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('room-categories/', views.room_list, name='room_list'),
    path('room-details/<int:pk>/', views.room_detail, name='room_detail'),
]
