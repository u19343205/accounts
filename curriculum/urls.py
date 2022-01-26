from django.urls import path
from  curriculum import views

app_name = 'curriculum'

urlpatterns = [

    path('ask/', views.askquestion, name ='ask a question'),
    path('', views.StandardlistView.as_view(), name ='standard_list'),
    path('<slug:slug>/', views.CourseListView.as_view(), name ='course_list'),
    ]
