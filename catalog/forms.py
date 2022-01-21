from django import forms 
from django.contrib.auth.models import Question, User


class QuestionForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User


    Assignment_Related = 'Assignment Related'
    Lecture_Related = 'Lecture Related'
    General = 'General'

    topics = [

    (Assignment_Related,'Assignment Related'),
    (Lecture_Related,  'Lecture Related'),
    (General, 'General'),
    ]
    
    topics = forms.ChoiceField(required=True, choices=topics)


    class Meta():
        model = Question 
        fields = ('topics', 'question',)


