from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from .forms import CreateUserForm, ForgotPasswordForm, ProfileUpdateForm

# Password Reset Request view
def password_reset_inquiry(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            associated_users = User.objects.filter(email=email)
            if len(associated_users) ==1 and associated_users[0].username == username:
                if associated_users[0] is not None:
                    return redirect('password_reset_verified',associated_users[0].username)
            else:
                form = ForgotPasswordForm()
                return render(request, 'accounts/password_reset_inquiry.html',
                              {'form': form,
                               'error':'Either the email or username was entered incorrectly. Please try again'})
    else:
        form = ForgotPasswordForm()
    return render(request, 'accounts/password_reset_inquiry.html',{'form': form})

# Password Reset View
def password_reset_verified(request,username):
    if request.method == 'POST':
        associated_user = User.objects.filter(username=username)
        form = SetPasswordForm(associated_user[0],data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'accounts/password_reset_verified.html', {'form': form})

# Profile Edit View
def profile_edit(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request,'accounts/profile_edit.html', {'form': form})

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
    if request.user.is_authenticated:
        return redirect('home-user')
    else:
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
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')