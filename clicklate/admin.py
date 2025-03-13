from django.contrib import admin
from .models import Clicklate, Translated

# if a new database table is added, you have to register here

admin.site.register(Clicklate)
admin.site.register(Translated)