from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView, TemplateView)
from .models import Answer, Course, Module, Question, Assignment, Lecture
from django.urls import reverse_lazy, reverse
from .forms import AnswerForm, QuestionForm, AssignmentForm, LectureForm
from django.http import HttpResponseRedirect
from django.db.models import Q


class CourseListView(ListView):
    context_object_name = 'courses'
    model = Course
    template_name = 'curriculum/course_list_view.html'

class ModuleListView(DetailView):
    context_object_name = 'courses'
    model = Course
    template_name = 'curriculum/module_list_view.html'

class QuestionListView(DetailView):
    context_object_name = 'modules'
    model = Module
    template_name = 'curriculum/question_list_view.html'

class AssignmentListView(DetailView):
    context_object_name = 'modules'
    model = Module
    template_name = 'curriculum/assignment_list_view.html'

class AssignmentDetailView(DetailView, FormView):
    context_object_name = 'assignments'
    model = Assignment
    template_name = 'curriculum/assignment_detail.html'
    form_class = AnswerForm

def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        module= self.object.module
        return reverse_lazy('curriculum:assignment_list',kwargs={'course':course.slug,
                                                             'module':module.slug,
                                                             'slug':self.object.slug})


class AssignmentCreateView(CreateView):
    form_class = AssignmentForm
    context_object_name = 'module'
    model= Module
    template_name = 'curriculum/assignment_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('curriculum:assignment_list',kwargs={'course':course.slug,
                                                             'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.course = self.object.course
        fm.module = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
    
class AssignmentUpdateView(UpdateView):
    fields = ('id','name','description','duedate')
    model = Assignment
    template_name = 'curriculum/assignment_update.html'
    context_object_name = 'assignments'


class LectureListView(DetailView):
    context_object_name = 'modules'
    model = Module
    template_name = 'curriculum/lecture_list_view.html'

class LectureDetailView(DetailView, FormView):
    context_object_name = 'lectures'
    model = Lecture
    template_name = 'curriculum/lecture_detail.html'
    form_class = LectureForm

def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        module= self.object.module
        return reverse_lazy('curriculum:lecture_list',kwargs={'course':course.slug,
                                                             'module':module.slug,
                                                             'slug':self.object.slug})

class LectureCreateView(CreateView):
    form_class = LectureForm
    context_object_name = 'module'
    model= Module
    template_name = 'curriculum/lecture_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('curriculum:assignment_list',kwargs={'course':course.slug,
                                                             'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.course = self.object.course
        fm.module = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
    
class LectureUpdateView(UpdateView):
    fields = ('id','name','teacher','slides', 'video', 'notes')
    model = Lecture
    template_name = 'curriculum/lecture_update.html'
    context_object_name = 'lectures'



class QuestionDetailView(DetailView, FormView):
    context_object_name = 'questions'
    model = Question
    template_name = 'curriculum/question_detail_view.html'
    form_class = AnswerForm
    #second_form_class = CommentForm
    #third_form_class = ReplyForm

    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        module = self.object.module
        return reverse_lazy('curriculum:question_detail',kwargs={'course':course.slug,
                                                             'module':module.slug,
                                                             'slug':self.object.slug})
    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.module = self.object.module
        fm.question = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class QuestionCreateView(CreateView):
    form_class = QuestionForm
    context_object_name = 'module'
    model= Module
    template_name = 'curriculum/question_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('curriculum:question_list',kwargs={'course':course.slug,
                                                             'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.course = self.object.course
        fm.module = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class QuestionUpdateView(UpdateView):
    fields = ('topics','subject','question','picture')
    model = Question
    template_name = 'curriculum/question_update.html'
    context_object_name = 'questions'

class QuestionDeleteView(DeleteView):
    model= Question
    context_object_name = 'questions'
    template_name = 'curriculum/question_delete.html'

    def get_success_url(self):
        print(self.object)
        course = self.object.course
        module = self.object.module
        return reverse_lazy('curriculum:question_list',kwargs={'course':course.slug,'slug':module.slug})

def search_questions(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(subject__icontains=query) | Q(question__icontains=query)

            results= Question.objects.filter(lookups).distinct()

            context={'results': results,
                    'submitbutton': submitbutton}

            return render(request, 'curriculum/search_questions.html', context)

        else:
                return render(request, 'curriculum/search_questions.html')

    else:
            return render(request, 'curriculum/search_questions.html')
