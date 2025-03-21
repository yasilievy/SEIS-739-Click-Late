from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import CreateUserForm


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
                return redirect('home')  # Redirect to the home page
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

def logout_view(request):
    logout(request)
    return redirect('login')

# Password Reset Request view
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # associated_user = User.objects.filter(email=email)
            # if associated_user.exists():
            #     user = associated_user[0]
            #     token = default_token_generator.make_token(user)
            #     uid = urlsafe_base64_encode(str(user.pk).encode())
            #     domain = get_current_site(request).domain
            #     link = f'http://{domain}/password_reset_confirm/{uid}/{token}/'

            #     # Send reset password email
            #     send_mail(
            #         'Password Reset Request',
            #         f'Click the following link to reset your password: {link}',
            #         'no-reply@mywebsite.com',
            #         [email],
            #         fail_silently=False,
            #     )
            #     messages.success(request, 'Password reset email sent!')
            #     return redirect('login')
            # else:
            #     messages.error(request, 'Email not found')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/password_reset.html', {'form': form})
