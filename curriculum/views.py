from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView, TemplateView)
from .models import Answer, Course, Module, Question, Assignment, Lecture
from django.urls import reverse_lazy, reverse
from .forms import AnswerForm, QuestionForm, AssignmentForm, LectureForm
from django.http import HttpResponseRedirect

#content object name refers to the related name in the models 
#create course view
class CourseListView(ListView):
    context_object_name = 'courses'
    model = Course
    template_name = 'curriculum/course_list_view.html'

#create module view
class ModuleListView(DetailView):
    context_object_name = 'courses'
    model = Course
    template_name = 'curriculum/module_list_view.html'

#create question list view
class QuestionListView(DetailView):
    context_object_name = 'modules'
    model = Module
    template_name = 'curriculum/question_list_view.html'

#create assignment list view
class AssignmentListView(DetailView):
    context_object_name = 'modules'
    model = Module
    template_name = 'curriculum/assignment_list_view.html'

#create assignment detail view 
#form view takes the assignment model and assignment form turns into a view
class AssignmentDetailView(DetailView, FormView):
    context_object_name = 'assignments'
    model = Assignment
    template_name = 'curriculum/assignment_detail.html'
    form_class = AssignmentForm

#as a detail view is inside a list view a reverse is required to go back to the list page 
#by using the slug fields this url allows for the next page to be rendered
def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        module= self.object.module
        return reverse_lazy('curriculum:assignment_list',kwargs={'course':course.slug,
                                                             'module':module.slug,
                                                             'slug':self.object.slug})

#assignment create view
class AssignmentCreateView(CreateView):
    form_class = AssignmentForm
    context_object_name = 'module'
    model= Module
    template_name = 'curriculum/assignment_create.html'

#as a create view is inside a list view a reverse is required to go back to the list page 
#by using the slug fields this url allows for the next page to be rendered
    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('curriculum:assignment_list',kwargs={'course':course.slug,
                                                             'slug':self.object.slug})
#the form must be vlaid for it to be posted. setting the objects, args and kwargs allows
#thehttpresponse to render the get success url 
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.course = self.object.course
        fm.module = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

  #create assignment update view  
class AssignmentUpdateView(UpdateView):
    fields = ('id','name','description','duedate') #show only these fields 
    model = Assignment
    template_name = 'curriculum/assignment_update.html'
    context_object_name = 'assignments'

#create lecture list view 
class LectureListView(DetailView):
    context_object_name = 'modules'
    model = Module
    template_name = 'curriculum/lecture_list_view.html'

#create lecture detail view 
#form view takes the lecture model and lecture form turns into a view
class LectureDetailView(DetailView, FormView):
    context_object_name = 'lectures'
    model = Lecture
    template_name = 'curriculum/lecture_detail.html'
    form_class = LectureForm

#as a create view is inside a list view a reverse is required to go back to the list page 
#by using the slug fields this url allows for the next page to be rendered
def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        module= self.object.module
        return reverse_lazy('curriculum:lecture_list',kwargs={'course':course.slug,
                                                             'module':module.slug,
                                                             'slug':self.object.slug})
#lecture create view
class LectureCreateView(CreateView):
    form_class = LectureForm
    context_object_name = 'module'
    model= Module
    template_name = 'curriculum/lecture_create.html'

#as a create view is inside a list view a reverse is required to go back to the list page 
#by using the slug fields this url allows for the next page to be rendered
    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('curriculum:assignment_list',kwargs={'course':course.slug,
                                                             'slug':self.object.slug})
#the form must be vlaid for it to be posted. setting the objects, args and kwargs allows
#thehttpresponse to render the get success url 
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.course = self.object.course
        fm.module = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

#create lecture update view  
class LectureUpdateView(UpdateView):
    fields = ('id','name','teacher','slides', 'video', 'notes') #only include these fields
    model = Lecture
    template_name = 'curriculum/lecture_update.html'
    context_object_name = 'lectures'

#create question detail view 
class QuestionDetailView(DetailView, FormView):
    context_object_name = 'questions'
    model = Question
    template_name = 'curriculum/question_detail_view.html'
    form_class = AnswerForm

#as a detail view is inside a list view a reverse is required to go back to the list page 
#by using the slug fields this url allows for the next page to be rendered
    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        module = self.object.module
        return reverse_lazy('curriculum:question_detail',kwargs={'course':course.slug,
                                                             'module':module.slug,
                                                             'slug':self.object.slug})
#the form must be vlaid for it to be posted. setting the objects, args and kwargs allows
#thehttpresponse to render the get success url 
    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.module = self.object.module
        fm.question = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

#create question view
class QuestionCreateView(CreateView):
    form_class = QuestionForm
    context_object_name = 'module'
    model= Module
    template_name = 'curriculum/question_create.html'

#as a create view is inside a list view a reverse is required to go back to the list page 
#by using the slug fields this url allows for the next page to be rendered
    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('curriculum:question_list',kwargs={'course':course.slug,
                                                             'slug':self.object.slug})
#the form must be vlaid for it to be posted. setting the objects, args and kwargs allows
#thehttpresponse to render the get success url 
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.course = self.object.course
        fm.module = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

#create update view for question model
class QuestionUpdateView(UpdateView):
    fields = ('topics','subject','question','picture') #only show these fields 
    model = Question
    template_name = 'curriculum/question_update.html'
    context_object_name = 'questions'


#question delete view 
class QuestionDeleteView(DeleteView):
    model= Question
    context_object_name = 'questions'
    template_name = 'curriculum/question_delete.html'

#as a create view is inside a list view a reverse is required to go back to the list page 
#by using the slug fields this url allows for the next page to be rendered
    def get_success_url(self):
        print(self.object)
        course = self.object.course
        module = self.object.module
        return reverse_lazy('curriculum:question_list',kwargs={'course':course.slug,'slug':module.slug})
