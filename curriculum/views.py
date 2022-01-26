from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from .models import Standard, Course, Module, Question
from django.urls import reverse_lazy
from .forms import CommentForm,AnswerForm, QuestionForm
from django.http import HttpResponseRedirect


class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'

class CourseListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/course_list_view.html'

class ModuleListView(DetailView):
    context_object_name = 'courses'
    model = Course
    template_name = 'curriculum/module_list_view.html'

class QuestionListView(DetailView):
    context_object_name = 'modules'
    model = Module
    template_name = 'curriculum/question_list_view.html'

class QuestionDetailView(DetailView, FormView):
    context_object_name = 'question'
    model = Question
    template_name = 'curriculum/lesson_detail_view.html'
    form_class = CommentForm
    second_form_class = AnswerForm

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


    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_detail',kwargs={'standard':standard.slug,
                                                             'subject':subject.slug,
                                                             'slug':self.object.slug})
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
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = QuestionForm
    context_object_name = 'subject'
    model= Course
    template_name = 'curriculum/question_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:question_list',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})


    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
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
