from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from django.contrib import messages

@login_required
def view_profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)

    # Only allow access if user is viewing their own profile or is staff
    if not request.user.is_authenticated or (request.user != profile_user and not request.user.is_staff):
        messages.warning(request, "You are not authorized to view this profile.")
        return redirect('mainsite:home')

    # Try to get user profile; if it doesn't exist, pass None
    user_profile = UserProfile.objects.filter(user=profile_user).first()

    return render(request, 'profiles/view_profile.html', {
        'profile_user': profile_user,
        'user_profile': user_profile,
        'is_owner': request.user == profile_user
    })
    

@login_required
def edit_profile(request):
    user = request.user
    is_admin = user.is_staff

    # Ensure UserProfile exists
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=user_profile) if not is_admin else None

        if user_form.is_valid() and (is_admin or profile_form.is_valid()):
            user_form.save()
            if profile_form:
                profile_form.save()
            return redirect('profiles:view_profile', user_id=user.id)

    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile) if not is_admin else None

    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user,
        'user_profile': user_profile,
        'is_admin': is_admin,
    })
