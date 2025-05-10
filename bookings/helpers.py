from .models import Booking, Room, RoomCategory


def check_room_availability(category_id, check_in, check_out):
    category = RoomCategory.objects.get(id=category_id)
    total_rooms = Room.objects.filter(
        category=category, is_available=True
    ).count()
    bookings = Booking.objects.filter(
        room_category=category, is_paid=True, is_cancelled=False
    )

    no_unavailable = 0  # Tracks how many overlapping bookings exist

    for booking in bookings:
        existing_check_in = booking.check_in
        existing_check_out = booking.check_out

        # Overlapping date logic
        if check_in < existing_check_out and check_out > existing_check_in:
            no_unavailable += 1

    # If fewer bookings than total rooms → still available
    if no_unavailable < total_rooms:
        return True
    else:
        return False
