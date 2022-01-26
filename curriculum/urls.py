from django.urls import path
from  curriculum import views

app_name = 'curriculum'

urlpatterns = [

    #path('ask/', views.askquestion, name ='ask a question'),
    path('', views.StandardListView.as_view(), name='standard_list'),
    path('<slug:slug>/', views.CourseListView.as_view(), name='course_list'),
    path('<str:standard>/<slug:slug>/', views.ModuleListView.as_view(), name='module_list'),
    path('<str:standard>/<str:slug>/create/', views.QuestionCreateView.as_view(),name='question_create'),
    path('<str:standard>/<str:subject>/<slug:slug>/', views.QuestionDetailView.as_view(),name='question_detail'),
    path('<str:standard>/<str:subject>/<slug:slug>/update/', views.QuestionUpdateView.as_view(),name='question_update'),
    path('<str:standard>/<str:subject>/<slug:slug>/delete/', views.QuestionDeleteView.as_view(),name='question_delete'),
    ]
