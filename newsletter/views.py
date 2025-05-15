from django.shortcuts import redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import Subscriber


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                Subscriber.objects.create(email=email)
                messages.success(
                    request,
                    'Thank you for subscribing to our newsletter!'
                )
            except Exception:
                messages.info(
                    request,
                    'You are already subscribed to our newsletter!'
                )
        else:
            messages.error(request, 'Invalid email address.')
    return redirect('mainsite:home')
