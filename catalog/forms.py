from django import forms 
from django.forms import fields
from catalog.models import Question


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
        