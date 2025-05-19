from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('mainsite.urls', namespace='mainsite')),
    path('', include('rooms.urls', namespace='rooms')),
    path('', include('profiles.urls', namespace='profiles')),
    path('booking/', include('bookings.urls', namespace='bookings')),
    path('customer/', include('customer.urls', namespace='customer')),
    path(
        'custom-admin/', include('custom_admin.urls', namespace='custom_admin')
        ),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
]
