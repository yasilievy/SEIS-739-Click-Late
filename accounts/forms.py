# from django.forms import ModelForm, Form, TextInput
from django import forms
from django.contrib.auth.models import User
# from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
# from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class EmailUserForm(PasswordResetForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    class Meta:
        model = User
        fields = ['username','email']
    