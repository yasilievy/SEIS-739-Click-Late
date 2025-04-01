from django.http import JsonResponse
from .models import Translated
from .serializers import TranslatedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def home_user(request,username):
    user = User.objects.filter(username=username)[0]
    return render(request, 'home-user.html',{'user':user})
