from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordMixin

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

class UpdatePasswordForm(forms.Form):
    email = forms.EmailField(
        label= ("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password1, password2 = SetPasswordMixin.create_password_fields()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']