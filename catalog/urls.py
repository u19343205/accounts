from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path 
from catalog import views 

urlpatterns = [
    path('', views.index, name ='index'),

]