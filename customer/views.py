from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from bookings.models import Booking

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user, is_paid=True).order_by('-created_at')
    return render(request, 'customer/dashboard.html', {'bookings': bookings})

@login_required
def booking_detail(request, booking_number):
    booking = get_object_or_404(Booking, booking_number=booking_number, user=request.user)
    return render(request, 'customer/booking_detail.html', {'booking': booking})
