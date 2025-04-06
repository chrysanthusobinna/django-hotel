from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

]
