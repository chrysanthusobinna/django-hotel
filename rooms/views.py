from django.shortcuts import render, get_object_or_404
from .models import RoomCategory

def room_list(request):
    rooms = RoomCategory.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(RoomCategory, pk=pk)
    return render(request, 'rooms/room_detail.html', {'room': room})
