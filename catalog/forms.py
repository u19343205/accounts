from django import forms 
from django.forms import fields
from catalog.models import Question, Student


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields =  (
            'topics',
            'subject',
            'question',
            'pub_date',
            'picture',
            
        )

from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_name',
        ]

class AddBook(forms.Form):
    titel = forms.CharField(widget=forms.TextInput())
    author = forms.CharField(widget=forms.TextInput())