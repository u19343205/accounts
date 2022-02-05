from django.test import TestCase
from django.template.defaultfilters import slugify
from curriculum.models import Question, User
from curriculum.forms import QuestionForm
import unittest

class TestAskQuestionForm(unittest.TestCase):
    def test_valid_form(self):
        """Tests to check whether the form is valid"""
        w = Question.objects.create(subject='Hello', body='Test')
        data = {'subject': w.subject, 'question': w.question}
        form = QuestionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Tests to check whether the form is invalid"""
        w = Question.objects.create(subject='Hello', body='Test')
        data = {'subject': w.subject, 'question': w.question,}
        form = QuestionForm(data=data)
        self.assertFalse(form.is_valid())