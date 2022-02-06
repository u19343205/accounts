"""config URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import  include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.decorators.vary import vary_on_cookie
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from catalog import views
from curriculum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')), #to include all urls from the catalog app
    path('curriculum/', include('curriculum.urls')), #to include all urls from the curriculum app
    path('accounts/', include('django.contrib.auth.urls')), #enables the log in and log in function to work from django authorisation

]
#This media handling will old be located here during WMGTSS testing. Throughout production media will be stored on a seperate server
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "WMGTSS Admin" #Changes admin name 
admin.site.site_title = "WMGTSS Admin Portal" #changes admin title 
