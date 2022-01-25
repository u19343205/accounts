from django.shortcuts import render
from django.http import HttpResponse
from catalog.forms import QuestionForm
from catalog.models import Question
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse('')

def askquestion(request):
    if request.POST:
        form = QuestionForm()
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect('ask.html')
        else:
            form = QuestionForm()
        context = {
            'questions': QuestionForm.objects.all(),
            "question_form": form,
    }
        context.update(request)
        return render(request, 'catalog/ask.html', context)