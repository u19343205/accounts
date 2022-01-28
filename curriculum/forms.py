from django import forms
from django.forms import fields
from curriculum.models import Question, Answer 


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['created_by', 'standard', 'created_at', 'course', 'slug']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"

'''
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer_body',)

        widgets = {
            'answer_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AnswerForm, self).__init__(*args, **kwargs)
'''