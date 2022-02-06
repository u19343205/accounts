from django import forms
from django.forms import fields, widgets
from curriculum.models import Question, Answer, Assignment, Lecture

#Take the question model and turn the fields into a model form 
#Class Meta which calls to change the behaviour of the ModelForm.
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        #excludes the following fields to appear on the form
        exclude = ['module','created_by', 'standard', 'created_at', 'course', 'slug', 'assignment', 'lecture']

#Take the answer model and turn the fields into a model form 
#Class Meta which calls to change the behaviour of the ModelForm.
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        #fields select on;y th body field to appear on the form
        fields = ['body']

#Take the assignment model and turn the fields into a model form 
#Class Meta which calls to change the behaviour of the ModelForm.
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        #excludes the following fields to appear on the form
        exclude = ['module', 'course', 'slug' ]

#Take the lecture model and turn the fields into a model form 
#Class Meta which calls to change the behaviour of the ModelForm.
class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        #excludes the following fields to appear on the form
        exclude = ['module', 'course', 'slug', 'created_at']
