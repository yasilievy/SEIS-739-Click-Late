from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging

from django.contrib.auth import authenticate, login, logout


logger = logging.getLogger(__name__)

def profile(request, format=None):
    # return HttpResponse('Home page')
    return render(request, 'accounts/profile.html')

def login(request, format=None):

    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('username')
        
    # return HttpResponse('Contact page')
    return render(request, 'accounts/login.html')

@api_view(['GET','PUT','DELETE','POST'])
def register(request, format=None):
    form = UserCreationForm()
    
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/register.html',context)