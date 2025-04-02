from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import CreateUserForm, EmailUserForm, EmailUpdateForm
from django.contrib.auth.models import User

def emailupdate_view(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_email = form.cleaned_data.get('new_email')
            old_email = form.cleaned_data.get('old_email')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user.email = new_email
                user.save()
                print(user.email)
                messages.success(request, f'successfully updated email to {new_email}!')
                return redirect('profile')
            else:
                print('incorrect login authentication')

    else:
        form = EmailUpdateForm(request.POST)
    return render(request,'accounts/email_update.html',{'form':form})




def profile_view(request):
    if request.user.is_authenticated:
        return render(request,'accounts/profile.html',{'user':request.user})
    return redirect('login')

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home-user')  # Redirect to the home page
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')

# Password Reset Request view
def password_reset_inquiry(request):
    hidden_bool = False
    if request.method == 'POST':
        form = EmailUserForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            associated_email = User.objects.filter(email=email)
            associated_user = associated_email[0]
            if associated_user.username == username and associated_user.check_password(password):
                return redirect('password_reset_verified',username=username)
            else:
                messages.error(request, 'Email not found')
    else:
        form = EmailUserForm()
    return render(request, 'accounts/password_reset_inquiry.html', {'form': form,'bool':hidden_bool})

def password_reset_verified(request, username):
    user = User.objects.filter(username=username)[0]
    if request.method == 'POST':
        form = SetPasswordForm(user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SetPasswordForm(user)
    return render(request, 'accounts/password_reset_verified.html', {'form': form})