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
from django.views.generic.base import TemplateView 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.decorators.vary import vary_on_cookie
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from catalog import views 
import catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalog', views.index, name='home.html'),
    path('accounts/login', TemplateView.as_view(template_name='login.html'), name='WMGTSS Login'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='WMGTSS Dashboard'), #Dashboard Link
    path('ask/', TemplateView.as_view(template_name='ask.html'), name='WMGTSS Q&A'), #Q&A Board
    path('test/', TemplateView.as_view(template_name='test.html'), name='WMGTSS Dashboard'),
    path('catalog/', TemplateView.as_view(template_name='home.html'), name='WMGTSS Dashboard'),
    



     
]
#This media handling will old be located here during WMGTSS testing. Throughout production media will be stored on a seperate server
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "WMGTSS Admin"
admin.site.site_title = "WMGTSS Admin Portal"

