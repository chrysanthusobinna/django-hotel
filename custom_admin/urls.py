from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('room-categories/', views.room_categories, name='room_categories'),
    path('room-category/<int:category_id>/', views.room_category_detail, name='room_category_detail'),
    path('room-category/add/', views.add_room_category, name='add_room_category'),
    path('room-category/<int:category_id>/edit/', views.edit_room_category, name='edit_room_category'),
    path('room-category/<int:category_id>/delete/', views.delete_room_category, name='delete_roomcategory'),

    
    path('room-category/<int:category_id>/add-additional-image/', views.add_additional_image, name='add_additional_image'),
    path('room-category/<int:category_id>/delete-additional-image/<int:image_id>/', views.delete_additional_image, name='delete_additional_image'),
] 