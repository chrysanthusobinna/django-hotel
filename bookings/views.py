from django.shortcuts import render, redirect, get_object_or_404
from rooms.models import RoomCategory
from datetime import datetime

def booking_summary(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')
        adults = request.POST.get('adults')
        children = request.POST.get('children')

        # Convert to date objects
        check_in = datetime.strptime(check_in_str, "%Y-%m-%d").date()
        check_out = datetime.strptime(check_out_str, "%Y-%m-%d").date()
        nights = (check_out - check_in).days

        room = get_object_or_404(RoomCategory, id=room_id)
        total_price = nights * room.price

        # Save in session
        request.session['booking'] = {
            'room_id': room_id,
            'check_in': check_in_str,  # Save string format for later reuse
            'check_out': check_out_str,
            'adults': adults,
            'children': children,
            'nights': nights,
            'total_price': float(total_price),
        }

        return redirect('bookings:booking_summary')

    # GET method - render booking summary
    booking = request.session.get('booking')
    if not booking:
        return redirect('mainsite:home')

    room = get_object_or_404(RoomCategory, id=booking['room_id'])

    # Convert check_in/out back to date object for formatting in template
    booking['check_in'] = datetime.strptime(booking['check_in'], "%Y-%m-%d").date()
    booking['check_out'] = datetime.strptime(booking['check_out'], "%Y-%m-%d").date()

    return render(request, 'bookings/booking_summary.html', {
        'room': room,
        'booking': booking,
    })
