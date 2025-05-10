from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from rooms.models import RoomCategory, RoomCategoryImage, Room
from .forms import RoomCategoryForm, RoomCategoryImageForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from bookings.models import Booking
from datetime import datetime
from django.db.models import Q


def is_admin(user):
    return user.is_staff

# Create your views here.


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def dashboard(request):
    return render(request, 'custom_admin/dashboard.html')


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def room_categories(request):
    categories = RoomCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(
        request,
        'custom_admin/room_categories.html',
        context
    )


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def room_category_detail(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    rooms = category.rooms.all()
    return render(request, 'custom_admin/room_category_detail.html', {
        'category': category,
        'rooms': rooms
    })


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def edit_room_category(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)

    if request.method == 'POST':
        form = RoomCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room category updated successfully!')
            return redirect(
                'custom_admin:room_category_detail',
                category_id=category.id
            )
    else:
        form = RoomCategoryForm(instance=category)

    # Get all additional images for this category
    additional_images = category.images.all()

    return render(request, 'custom_admin/edit_room_category.html', {
        'form': form,
        'category': category,
        'additional_images': additional_images
    })


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def delete_room_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(RoomCategory, id=category_id)
        category.delete()
        messages.success(request, 'Room category deleted successfully!')
    return redirect('custom_admin:room_categories')


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def add_additional_image(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)

    if request.method == 'POST':
        form = RoomCategoryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.room_category = category
            image.save()
            messages.success(request, 'Additional image added successfully!')
            return redirect(
                'custom_admin:edit_room_category',
                category_id=category.id
            )
        else:
            messages.error(
                request,
                'Error adding image. Please check the form.'
            )
            return redirect(
                'custom_admin:edit_room_category',
                category_id=category.id
            )

    return redirect('custom_admin:edit_room_category', category_id=category.id)


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def delete_additional_image(request, category_id, image_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    image = get_object_or_404(
        RoomCategoryImage,
        id=image_id,
        room_category=category
    )

    if request.method == 'POST':
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect(
            'custom_admin:edit_room_category',
            category_id=category.id
        )

    return redirect(
        'custom_admin:edit_room_category',
        category_id=category.id
    )


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def add_room_category(request):
    if request.method == 'POST':
        form = RoomCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Room category created successfully!')
            return redirect(
                'custom_admin:edit_room_category',
                category_id=category.id
            )
    else:
        form = RoomCategoryForm()

    return render(request, 'custom_admin/add_room_category.html', {
        'form': form
    })


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def add_room(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        is_available = request.POST.get('is_available') == 'on'

        try:
            category = RoomCategory.objects.get(id=category_id)
            room = Room.objects.create(
                category=category,
                name=name,
                is_available=is_available
            )
            messages.success(request, 'Room added successfully!')
            return redirect(
                'custom_admin:room_category_detail',
                category_id=category_id
            )
        except RoomCategory.DoesNotExist:
            messages.error(request, 'Invalid room category.')
            return redirect(
                'custom_admin:room_category_detail',
                category_id=category_id
            )
        except Exception as e:
            messages.error(request, f'Error adding room: {str(e)}')
            return redirect(
                'custom_admin:room_category_detail',
                category_id=category_id
            )

    return redirect('custom_admin:room_categories')


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        is_available = request.POST.get('is_available') == 'on'

        try:
            room.name = name
            room.is_available = is_available
            room.save()
            messages.success(request, 'Room updated successfully!')
            return redirect(
                'custom_admin:room_category_detail',
                category_id=room.category.id
            )
        except Exception as e:
            messages.error(request, f'Error updating room: {str(e)}')
            return redirect(
                'custom_admin:room_category_detail',
                category_id=room.category.id
            )

    return redirect(
        'custom_admin:room_category_detail',
        category_id=room.category.id
    )


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def delete_room(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(Room, id=room_id)
        category_id = room.category.id
        try:
            room.delete()
            messages.success(request, 'Room deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting room: {str(e)}')
        return redirect(
            'custom_admin:room_category_detail',
            category_id=category_id
        )

    return redirect(
        'custom_admin:room_category_detail',
        category_id=room.category.id
    )


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def booking_list(request):
    bookings = Booking.objects.all().order_by('-created_at')
    context = {
        'bookings': bookings
    }
    return render(
        request,
        'custom_admin/booking_list.html',
        context
    )


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Get available rooms for the booking's category
    available_rooms = Room.objects.filter(
        category=booking.room_category,
        is_available=True
    ).exclude(
        id__in=Booking.objects.filter(
            ~Q(id=booking_id),
            ~Q(is_cancelled=True),
            room__isnull=False,
            check_in__lte=booking.check_out,
            check_out__gte=booking.check_in
        ).values_list('room_id', flat=True)
    )

    return render(request, 'custom_admin/booking_detail.html', {
        'booking': booking,
        'available_rooms': available_rooms
    })


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def update_checkin(request):
    if request.method == 'POST':
        try:
            booking_id = request.POST.get('booking_id')
            check_in_datetime = request.POST.get('check_in_datetime')

            booking = get_object_or_404(Booking, id=booking_id)
            naive_datetime = datetime.strptime(
                check_in_datetime,
                '%Y-%m-%dT%H:%M'
            )
            booking.actual_check_in = timezone.make_aware(naive_datetime)
            booking.save()

            messages.success(request, 'Check-in time updated successfully')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )
        except Exception as e:
            messages.error(request, f'Error updating check-in time: {str(e)}')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )

    return redirect('custom_admin:booking_list')


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def update_checkout(request):
    if request.method == 'POST':
        try:
            booking_id = request.POST.get('booking_id')
            check_out_datetime = request.POST.get('check_out_datetime')

            booking = get_object_or_404(Booking, id=booking_id)
            naive_datetime = datetime.strptime(
                check_out_datetime,
                '%Y-%m-%dT%H:%M'
            )
            booking.actual_check_out = timezone.make_aware(naive_datetime)
            booking.save()

            messages.success(request, 'Check-out time updated successfully')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )
        except Exception as e:
            messages.error(request, f'Error updating check-out time: {str(e)}')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )

    return redirect('custom_admin:booking_list')


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def cancel_booking(request):
    if request.method == 'POST':
        try:
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id)
            booking.is_cancelled = True
            booking.save()

            messages.success(request, 'Booking cancelled successfully')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )
        except Exception as e:
            messages.error(request, f'Error cancelling booking: {str(e)}')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )

    return redirect('custom_admin:booking_list')


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def delete_booking(request):
    if request.method == 'POST':
        try:
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id)
            booking.delete()

            messages.success(request, 'Booking deleted successfully')
            return redirect('custom_admin:booking_list')
        except Exception as e:
            messages.error(request, f'Error deleting booking: {str(e)}')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )

    return redirect('custom_admin:booking_list')


@login_required
@user_passes_test(is_admin, login_url='mainsite:home')
def assign_room(request):
    if request.method == 'POST':
        try:
            booking_id = request.POST.get('booking_id')
            room_id = request.POST.get('room_id')

            booking = get_object_or_404(Booking, id=booking_id)
            room = get_object_or_404(Room, id=room_id)

            # Verify room is in the same category as the booking
            if room.category != booking.room_category:
                messages.error(
                    request,
                    'Selected room is not in the same category as the booking'
                )
                return redirect(
                    'custom_admin:booking_detail',
                    booking_id=booking_id
                )

            # Check if room is available for the booking dates
            conflicting_booking = Booking.objects.filter(
                ~Q(id=booking_id),  # Exclude current booking
                ~Q(is_cancelled=True),  # Exclude cancelled bookings
                room=room,
                check_in__lte=booking.check_out,
                check_out__gte=booking.check_in
            ).first()

            if conflicting_booking:
                messages.error(
                    request,
                    'Room is already booked for these dates'
                )
                return redirect(
                    'custom_admin:booking_detail',
                    booking_id=booking_id
                )

            # Assign the room
            booking.room = room
            booking.save()

            messages.success(request, 'Room assigned successfully')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )

        except Exception as e:
            messages.error(request, f'Error assigning room: {str(e)}')
            return redirect(
                'custom_admin:booking_detail',
                booking_id=booking_id
            )

    return redirect('custom_admin:booking_list')
