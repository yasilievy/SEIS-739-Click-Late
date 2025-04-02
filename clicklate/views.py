from django.http import JsonResponse
from .models import Translated
from .serializers import TranslatedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def home_user(request):
    if request.user.is_authenticated:
        return render(request, 'home-user.html',{'user':request.user})
    return redirect('home')
