from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import RoomCategory
from profiles.models import UserProfile


def room_list(request):
    room_categories = RoomCategory.objects.all()
    return render(request, 'rooms/room_list.html', {
        'room_categories': room_categories,
        'SITE_NAME': settings.SITE_NAME
    })


def room_detail(request, pk):
    room_category = get_object_or_404(RoomCategory, pk=pk)

    user = request.user
    can_book = user.is_authenticated and not user.is_staff
    incomplete_profile = False

    if can_book:
        try:
            profile = user.profile
            if not all([
                profile.address,
                profile.city,
                profile.post_code,
                profile.country
            ]):
                incomplete_profile = True
        except UserProfile.DoesNotExist:
            incomplete_profile = True

    return render(request, 'rooms/room_detail.html', {
        'room_category': room_category,
        'can_book': can_book,
        'incomplete_profile': incomplete_profile,
    })
