from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('room-categories/', views.room_categories, name='room_categories'),
    path('room-category/<int:category_id>/',
         views.room_category_detail, name='room_category_detail'),
    path('room-category/add/',
         views.add_room_category, name='add_room_category'),
    path('room-category/<int:category_id>/edit/',
         views.edit_room_category, name='edit_room_category'),
    path('room-category/<int:category_id>/delete/',
         views.delete_room_category, name='delete_roomcategory'),

    path('room-category/<int:category_id>/add-additional-image/',
         views.add_additional_image, name='add_additional_image'),
    path('room-category/<int:category_id>/'
         'delete-additional-image/<int:image_id>/',
         views.delete_additional_image, name='delete_additional_image'),

    path('room/add/', views.add_room, name='add_room'),
    path('room/<int:room_id>/edit/',
         views.edit_room, name='edit_room'),
    path('room/<int:room_id>/delete/',
         views.delete_room, name='delete_room'),

    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/',
         views.booking_detail, name='booking_detail'),
    path('update-checkin/', views.update_checkin, name='update_checkin'),
    path('update-checkout/', views.update_checkout, name='update_checkout'),
    path('cancel-booking/', views.cancel_booking, name='cancel_booking'),
    path('delete-booking/', views.delete_booking, name='delete_booking'),
    path('assign-room/', views.assign_room, name='assign_room'),
]
