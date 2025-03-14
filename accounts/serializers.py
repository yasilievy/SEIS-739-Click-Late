from rest_framework import serializers
from .models import UserProfile

# need to add database table here too
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['firstname','lastname','email','username','password']