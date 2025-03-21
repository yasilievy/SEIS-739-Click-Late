from django.http import JsonResponse
from .models import Translated
from .serializers import TranslatedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

