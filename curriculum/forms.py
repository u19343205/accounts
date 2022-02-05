from django import forms
from django.forms import fields, widgets
from curriculum.models import Question, Answer, Assignment, Lecture


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        options = [
        ('Yes','Yes'),
        ('No','No'),
        ]
        anonymous = forms.CharField(label ="Submit Anonymously", widget=forms.RadioSelect(choices=options))
        exclude = ['module','created_by', 'standard', 'created_at', 'course', 'slug', 'assignment', 'lecture']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['module', 'course', 'slug' ]

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        exclude = ['module', 'course', 'slug', 'created_at']
'''
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {"body":"Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ReplyForm, self).__init__(*args, **kwargs)
'''