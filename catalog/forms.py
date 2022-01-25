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
            'picture',
            
        )
