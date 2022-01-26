from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, DetailView,
                                    ListView, FormView)
from curriculum.models import Standard, Course
from curriculum.forms import QuestionForm
from curriculum.models import Question

class StandardlistView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'

class CourseListView(ListView):
    context_object_name = 'Course'
    model = Course
    template_name = 'curriculum/course_list_view.html'


def get_context_data(self, **kwargs):
        context = super(StandardlistView, self).get_context_data(**kwargs)
        context['standard'] = Standard.objects.all()
        return context

def askquestion(request):
    context = {}
    form = QuestionForm(data=request.POST)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    context['form'] = form
    return render(request, "curriculum/ask.html", context)