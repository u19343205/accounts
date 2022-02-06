from django.urls import path
from curriculum import views
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView, TemplateView)

app_name = 'curriculum'

urlpatterns = [

    path('', views.CourseListView.as_view(), name='course_list'), #when qna page sleected it goes directly to course view
    path('<slug:slug>/', views.ModuleListView.as_view(), name='module_list'), #which course is chosen will become a slug and the module list vie will appear
    path('<str:course>/<slug:slug>/', views.QuestionListView.as_view(), name='question_list'), #when a module is chosen questions asked for that module will appear with the course and module as a slug
    path('<str:course>/<str:slug>/assignments', views.AssignmentListView.as_view(), name='assignment_list'), #when view assignments is selected 
    path('<str:course>/<str:slug>/lectures', views.LectureListView.as_view(), name='lecture_list'), #when lecture page is selected, lectures within a module will appear with the course and module as a slug
    path('<str:course>/<str:slug>/addassignment/', views.AssignmentCreateView.as_view(),name='assignment_create'), #when create view is selected the slug will be the course and module
    path('<str:course>/<str:slug>/addlecture/', views.LectureCreateView.as_view(),name='lecture_create'), #when create view is selected the slug will be the course and module
    path('<str:course>/<str:module>/<slug:slug>/assignments/', views.AssignmentDetailView.as_view(),name='assignment_detail'),#detail view the show course and module slug as well as the assignment name
    path('<str:course>/<str:module>/<slug:slug>/lectures/', views.LectureDetailView.as_view(),name='lecture_detail'), #detail view the show course and module slug as well as the lecture name
    path('<str:course>/<str:module>/<slug:slug>/updateassignment/', views.AssignmentUpdateView.as_view(),name='assignment_update'),  #update view will slug course, module as well as the assignment that is being updated
    path('<str:course>/<str:module>/<slug:slug>/updatelecture/', views.LectureUpdateView.as_view(),name='lecture_update'), #update view will slug course, module as well as the lecture that is being updated
    path('<str:course>/<str:slug>/ask/', views.QuestionCreateView.as_view(),name='question_create'), #when create view is selected the slug will be the course and module
    path('<str:course>/<str:module>/<slug:slug>/', views.QuestionDetailView.as_view(),name='question_detail'), #detail view the show course and module slug as well as the question subject
    path('<str:course>/<str:module>/<slug:slug>/update/', views.QuestionUpdateView.as_view(),name='question_update'),  #update view will slug course, module as well as the question that is being updated
    path('<str:course>/<str:module>/<slug:slug>/delete/', views.QuestionDeleteView.as_view(),name='question_delete'), #delete view will slug course, module as well as the question that is being deleted
    ]
