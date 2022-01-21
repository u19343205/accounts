from django.shortcuts import render
from django.http import HttpResponse

from catalog.forms import QuestionForm
from catalog.models import Question
from django.urls import reverse

def index(request):
    return HttpResponse ('home.html')


def askquestion(request):

    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)

        if question_form.is_valid():
            Question = question_form.save()

        else:
            print(question_form.errors)


    else:
        question_form = QuestionForm()

    return render(request, 'qna.html',{'question_form':QuestionForm})


