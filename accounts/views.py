from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def profile(request, format=None):
    # return HttpResponse('Home page')
    return render(request, 'accounts/profile.html')

def login(request, format=None):

    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('username')
        
    # return HttpResponse('Contact page')
    return render(request, 'accounts/login.html')

# @api_view(['GET','PUT','DELETE','POST'])
def register(request, format=None):
    form = CreateUserForm()
    
    
    # if request.method == 'POST':
    #     form = CreateUserForm(request.POST)

    #     if form.is_valid():
    #         form.save()

    context = {'form':form}
    return render(request, 'accounts/register.html',context)
