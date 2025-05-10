from django.urls import path
from . import views

app_name = 'newsletter'

# Newsletter subscription URLs
urlpatterns = [
    path(
        'subscribe/',
        views.subscribe_newsletter,
        name='subscribe_newsletter'
    ),
]
