from django.contrib import admin
from .models import Translated

# if a new database table is added, you have to register here
admin.site.register(Translated)