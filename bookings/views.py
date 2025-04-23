import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from rooms.models import RoomCategory
from .models import Booking
from datetime import datetime, date
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .helpers import check_room_availability


stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def booking_summary(request):
    if request.method == 'POST':
        room_category_id = request.POST.get('room_category_id')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')
        adults = request.POST.get('adults')
        children = request.POST.get('children')

        # Check if room category exists and has available rooms
        try:
            room_category = RoomCategory.objects.get(id=room_category_id)
            available_rooms = room_category.rooms.filter(is_available=True)
            if not available_rooms.exists():
                messages.error(request, "No rooms available in this category.")
                return redirect('rooms:room_detail', pk=room_category_id)
        except RoomCategory.DoesNotExist:
            messages.error(request, "Invalid room category selected.")
            return redirect('rooms:room_list')

        try:
            check_in = datetime.strptime(check_in_str, "%Y-%m-%d").date()
            check_out = datetime.strptime(check_out_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            messages.error(request, "Invalid check-in or check-out date.")
            return redirect('rooms:room_detail', pk=room_category_id)

        if check_in >= check_out:
            messages.error(request, "Check-out date must be after check-in.")
            return redirect('rooms:room_detail', pk=room_category_id)

        if check_in == check_out:
            messages.error(request, "Check-in and check-out cannot be on the same day.")
            return redirect('rooms:room_detail', pk=room_category_id)

        if check_in < date.today():
            messages.error(request, "Check-in date cannot be in the past.")
            return redirect('rooms:room_detail', pk=room_category_id)


        nights = (check_out - check_in).days
        total_price = nights * room_category.price

        # Check room availability
        is_available = check_room_availability(room_category_id, check_in, check_out)

        if is_available:
            # Save booking data in session
            request.session['booking'] = {
                'room_category_id': room_category_id,
                'check_in': check_in_str,
                'check_out': check_out_str,
                'adults': adults,
                'children': children,
                'nights': nights,
                'total_price': float(total_price),
            }

            return redirect('bookings:booking_summary')

        else:
            messages.error(request, "No available rooms in this category for the selected date range.")
            return redirect('rooms:room_detail', pk=room_category_id)


    # GET request – render booking summary
    booking = request.session.get('booking')
    if not booking:
        return redirect('mainsite:home')

    room_category = get_object_or_404(RoomCategory, id=booking['room_category_id'])

    # Convert date strings to date objects for display
    booking['check_in'] = datetime.strptime(booking['check_in'], "%Y-%m-%d").date()
    booking['check_out'] = datetime.strptime(booking['check_out'], "%Y-%m-%d").date()

    return render(request, 'bookings/booking_summary.html', {
        'room_category': room_category,
        'booking': booking,
    })


@login_required
def create_checkout_session(request):
    booking_data = request.session.get('booking')
    if not booking_data:
        return redirect('mainsite:home')

    # Fetch data
    room_category_id = booking_data['room_category_id']
    total_price = booking_data['total_price']
    check_in = booking_data['check_in']
    check_out = booking_data['check_out']

    room_category = get_object_or_404(RoomCategory, id=room_category_id)

    # Create Booking
    booking = Booking.objects.create(
        user=request.user,
        room_category=room_category,
        check_in=check_in,
        check_out=check_out,
        is_paid=False,
        total_price=total_price,
    )

    # Save booking ID and number to session for use after payment
    booking_data['booking_id'] = booking.id
    booking_data['booking_number'] = booking.booking_number
    request.session['booking'] = booking_data

    # Stripe payment session
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card', 'paypal', 'revolut_pay'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': f"Room Booking - {room_category.name}",
                    },
                    'unit_amount': int(float(total_price) * 100),  # in pence
                },
                'quantity': 1,
            }],
            mode='payment',
            customer_email=request.user.email,
            success_url=request.build_absolute_uri(reverse('bookings:payment_success')),
            cancel_url=request.build_absolute_uri(reverse('bookings:payment_cancelled')),
        )
        return redirect(session.url)
    except Exception as e:
        return JsonResponse({'error': str(e)})


@login_required
def payment_success(request):
    booking_data = request.session.get('booking')
    if not booking_data:
        return redirect('mainsite:home')

    try:
        booking = Booking.objects.get(id=booking_data['booking_id'], user=request.user)
    except Booking.DoesNotExist:
        return redirect('mainsite:home')

    if not booking.is_paid:
        booking.is_paid = True
        booking.save()

        # Send confirmation email
        subject = f"Booking Confirmation - #{booking.booking_number}"
        message = (
            f"Hi {request.user.first_name},\n\n"
            f"Thank you for your booking!\n\n"
            f"Booking Details:\n"
            f"Booking Number: {booking.booking_number}\n"
            f"Room Category: {booking.room_category.name}\n"
            f"Check-in: {booking.check_in}\n"
            f"Check-out: {booking.check_out}\n"
            f"Total Paid: ${booking.total_price}\n\n"
            f"We look forward to your stay!"
        )
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False
        )

    try:
        room_category = RoomCategory.objects.get(id=booking_data['room_category_id'])
    except RoomCategory.DoesNotExist:
        return redirect('mainsite:home')

    return render(request, 'bookings/payment_success.html', {
        'booking': booking,
        'room_category': room_category,
    })


def payment_cancelled(request):
    messages.warning(request, 'Payment was cancelled. You can try again.')
    return render(request, 'bookings/payment_cancelled.html', {
        'message': 'Payment was cancelled. You can try again.'
    })
