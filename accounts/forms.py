# from django.forms import ModelForm, Form, TextInput
from django import forms
from django.contrib.auth.models import User
# from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm,SetPasswordMixin
# from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    # password1, password2 = SetPasswordMixin.create_password_fields()
    class Meta:
        model = User
        fields = ['username','email']

class EmailUpdateForm(forms.Form):
    old_email = forms.EmailField(
        label= ("Old Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    new_email = forms.EmailField(
        label= ("New Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))

    password1, password2 = SetPasswordMixin.create_password_fields()

    class Meta:
        model = User
        fields = ['new email','old email','username','password1','password2']