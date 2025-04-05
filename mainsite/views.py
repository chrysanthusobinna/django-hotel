from django.shortcuts import render

def home_view(request):
    return render(request, 'mainsite/home.html')

def about_view(request):
    return render(request, 'mainsite/about.html')

def contact_view(request):
    return render(request, 'mainsite/contact.html')
