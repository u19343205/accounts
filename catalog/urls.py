from django.urls import path
from . import views
from django.views.generic import (TemplateView, DetailView,
                                    ListView, FormView)

urlpatterns = [
path ('', views.index, name='WMGTSS Dashboard'),


]
