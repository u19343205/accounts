from django import forms 
from django.forms import fields
from curriculum.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['pub_date']
     
