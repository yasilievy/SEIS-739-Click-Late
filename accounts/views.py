from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

def profile(request, format=None):
    # return HttpResponse('Home page')
    return render(request, 'accounts/profile.html')

def login(request, format=None):
    # return HttpResponse('Contact page')
    return render(request, 'accounts/login.html')

def register(request, format=None):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/register.html',context)