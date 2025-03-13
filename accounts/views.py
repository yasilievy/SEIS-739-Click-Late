from django.shortcuts import render
from django.http import HttpResponse

def profile(request, format=None):
    # return HttpResponse('Home page')
    return render(request, 'accounts/profile.html')

def login(request, format=None):
    # return HttpResponse('Contact page')
    return render(request, 'accounts/login.html')

def register(request, format=None):
    # return HttpResponse('Profile page')
    return render(request, 'accounts/register.html')