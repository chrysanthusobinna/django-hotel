
import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from rooms.models import RoomCategory
from .models import Booking
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def booking_summary(request):
    if request.method == 'POST':
        room_category_id = request.POST.get('room_category_id')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')
        adults = request.POST.get('adults')
        children = request.POST.get('children')

        # Convert to date objects
        check_in = datetime.strptime(check_in_str, "%Y-%m-%d").date()
        check_out = datetime.strptime(check_out_str, "%Y-%m-%d").date()
        nights = (check_out - check_in).days

        room_category = get_object_or_404(RoomCategory, id=room_category_id)
        total_price = nights * room_category.price

        # Create a Booking record
        booking = Booking.objects.create(
            user=request.user,
            room_category=room_category,
            check_in=check_in,
            check_out=check_out,
            is_paid=False,
            total_price=total_price
        )

        # Save in session
        request.session['booking'] = {
            'booking_id': booking.id,
            'booking_number': booking.booking_number,
            'room_category_id': room_category_id,
            'check_in': check_in_str,
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

    room_category = get_object_or_404(RoomCategory, id=booking['room_category_id'])

    # Convert check_in/out back to date object for formatting in template
    booking['check_in'] = datetime.strptime(booking['check_in'], "%Y-%m-%d").date()
    booking['check_out'] = datetime.strptime(booking['check_out'], "%Y-%m-%d").date()

    return render(request, 'bookings/booking_summary.html', {
        'room_category': room_category,
        'booking': booking,
    })

@login_required
def create_checkout_session(request):
    booking = request.session.get('booking')
    if not booking:
        return redirect('mainsite:home')

    room_category_id = booking['room_category_id']
    total_price = booking['total_price']

    # Get the room category object
    room_category = get_object_or_404(RoomCategory, id=room_category_id)

    # Get logged-in user details
    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card', 'paypal', 'revolut_pay'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': f"Room Booking - {room_category.name}",
                    },
                    'unit_amount': int(float(total_price) * 100),  # Stripe accepts amount in pence
                },
                'quantity': 1,
            }],
            mode='payment',
            customer_email=email,
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

    booking = get_object_or_404(Booking, id=booking_data['booking_id'], user=request.user)

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

    room_category = get_object_or_404(RoomCategory, id=booking_data['room_category_id'])

    return render(request, 'bookings/payment_success.html', {
        'booking': booking,
        'room_category': room_category,
    })


def payment_cancelled(request):
    return render(request, 'bookings/payment_cancelled.html')
