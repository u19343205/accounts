from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [

    path('ask/', views.askquestion, name ='ask a question')
    ]
