from django.forms import ModelForm
from .models import UserProfile
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class CreateUserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstname','lastname','username','email','password']
