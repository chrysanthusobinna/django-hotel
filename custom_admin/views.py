from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rooms.models import RoomCategory, RoomCategoryImage, Room
from .forms import RoomCategoryForm, RoomCategoryImageForm
from django.http import JsonResponse

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'custom_admin/dashboard.html')

@login_required
def room_categories(request):
    categories = RoomCategory.objects.all()
    return render(request, 'custom_admin/room_categories.html', {'categories': categories})

@login_required
def room_category_detail(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    rooms = category.rooms.all()
    return render(request, 'custom_admin/room_category_detail.html', {
        'category': category,
        'rooms': rooms
    })

@login_required
def edit_room_category(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    
    if request.method == 'POST':
        form = RoomCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room category updated successfully!')
            return redirect('custom_admin:room_category_detail', category_id=category.id)
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
def delete_room_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(RoomCategory, id=category_id)
        category.delete()
        messages.success(request, 'Room category deleted successfully!')
    return redirect('custom_admin:room_categories')



 
@login_required
def add_additional_image(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    
    if request.method == 'POST':
        form = RoomCategoryImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.room_category = category
            image.save()
            messages.success(request, 'Additional image added successfully!')
            return redirect('custom_admin:edit_room_category', category_id=category.id)
        else:
            messages.error(request, 'Error adding image. Please check the form.')
            return redirect('custom_admin:edit_room_category', category_id=category.id)
    
    return redirect('custom_admin:edit_room_category', category_id=category.id)

@login_required
def delete_additional_image(request, category_id, image_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    image = get_object_or_404(RoomCategoryImage, id=image_id, room_category=category)
    
    if request.method == 'POST':
        image.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect('custom_admin:edit_room_category', category_id=category.id)
    
    return redirect('custom_admin:edit_room_category', category_id=category.id)

@login_required
def add_room_category(request):
    if request.method == 'POST':
        form = RoomCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Room category created successfully!')
            return redirect('custom_admin:edit_room_category', category_id=category.id)
    else:
        form = RoomCategoryForm()
    
    return render(request, 'custom_admin/add_room_category.html', {
        'form': form
    })

@login_required
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
            return redirect('custom_admin:room_category_detail', category_id=category_id)
        except RoomCategory.DoesNotExist:
            messages.error(request, 'Invalid room category.')
            return redirect('custom_admin:room_categories')
        except Exception as e:
            messages.error(request, f'Error adding room: {str(e)}')
            return redirect('custom_admin:room_category_detail', category_id=category_id)
    
    return redirect('custom_admin:room_categories')

@login_required
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
            return redirect('custom_admin:room_category_detail', category_id=room.category.id)
        except Exception as e:
            messages.error(request, f'Error updating room: {str(e)}')
            return redirect('custom_admin:room_category_detail', category_id=room.category.id)
    
    return redirect('custom_admin:room_category_detail', category_id=room.category.id)

@login_required
def delete_room(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(Room, id=room_id)
        category_id = room.category.id
        try:
            room.delete()
            messages.success(request, 'Room deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting room: {str(e)}')
        return redirect('custom_admin:room_category_detail', category_id=category_id)
    
    return redirect('custom_admin:room_categories')
