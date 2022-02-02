from django.urls import path
from curriculum import views
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView, TemplateView)

app_name = 'curriculum'

urlpatterns = [

    path('qna/ask/', views.QuestionListView.as_view(), name='question_list'),
    path('qna/', TemplateView.as_view(template_name='qna.html'), name='WMGTSS Q&A'), #Q&A Board
    path('', views.CourseListView.as_view(), name='course_list'),
    path('search/', views.search_questions, name='search_questions'),
    path('<slug:slug>/', views.ModuleListView.as_view(), name='module_list'),
    path('<str:course>/<slug:slug>/', views.QuestionListView.as_view(), name='question_list'),
    path('<str:course>/<str:slug>/assignments', views.AssignmentListView.as_view(), name='assignment_list'),
    path('<str:course>/<str:slug>/addassignment/', views.AssignmentCreateView.as_view(),name='assignment_create'),
    path('<str:course>/<str:module>/<slug:slug>/assignments', views.AssignmentDetailView.as_view(),name='assignment_detail'),
    path('<str:course>/<str:slug>/create/', views.QuestionCreateView.as_view(),name='question_create'),
    path('<str:course>/<str:module>/<slug:slug>/', views.QuestionDetailView.as_view(),name='question_detail'),
    path('<str:course>/<str:module>/<slug:slug>/update/', views.QuestionUpdateView.as_view(),name='question_update'),
    path('<str:course>/<str:module>/<slug:slug>/delete/', views.QuestionDeleteView.as_view(),name='question_delete'),
    ]
