from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView, TemplateView)
from .models import Course, Module, Question
from django.urls import reverse_lazy, reverse
from .forms import CommentForm,AnswerForm, QuestionForm
from django.http import HttpResponseRedirect

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

def get_success_url(self):
        self.object = self.get_object()
        course = self.object.Course
        module= self.object.Module
        return reverse_lazy('curriculum:lesson_detail',kwargs={'course':course.slug,
                                                             'module':module.slug,
                                                             'slug':self.object.slug})


class QuestionDetailView(DetailView):
    context_object_name = 'questions'
    model = Question
    template_name = 'curriculum/question_detail.html'
    slug_url_kwarg = 'slug'
    #form_class = CommentForm
    #second_form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(request=self.request)
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name=='form' and form.is_valid():
            print("commented")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("answered")
            return self.form2_valid(form)


    
    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.question = self.object.comments.name
        fm.question_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
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
    context_object_name = 'question'
    template_name = 'curriculum/question_delete.html'

    def get_success_url(self):
        print(self.object)
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:question_list',kwargs={'standard':standard.slug,'slug':subject.slug})
