from django.shortcuts import render, get_object_or_404
from .models import RoomCategory

def room_list(request):
    room_categories = RoomCategory.objects.all()
    return render(request, 'rooms/room_list.html', {'room_categories': room_categories})


def room_detail(request, pk):
    room_category = get_object_or_404(RoomCategory, pk=pk)

    user = request.user
    can_book = user.is_authenticated and not user.is_staff

    return render(request, 'rooms/room_detail.html', {
        'room_category': room_category,
        'can_book': can_book,
    })
