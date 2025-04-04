"""
URL configuration for clicklate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clicklate import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home_user, name='home-user'),
    path('admin/', admin.site.urls),
    path('',include ('accounts.urls')), # taking urls py from a different app folder

]


url_patterns = format_suffix_patterns(urlpatterns) # getting JSON through browser