from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm
from .forms import AddBook
from catalog.models import Question
from django.http import HttpResponseRedirect

 
def addbook(request):
   form = AddBook()
   return render(request,'test.html',{'form':form})

def index(request):
    return HttpResponse('')


def askquestion(request):
    if request.POST:
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save(commit=False)
            return HttpResponseRedirect('/')

        else:
            question_form = QuestionForm
        context = {
            'questions': QuestionForm.objects.all(),
            "question_form": question_form,
            'username': auth.get_user(request).username,
    }
        context.update(csrf(request))
        return render(request, 'test.html', context)