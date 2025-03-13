from django.contrib import admin
from .models import UserProfile

# if a new database table is added, you have to register here

admin.site.register(UserProfile)