
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.test import Client, TestCase, override_settings
from ..curriculum.models import Question 
from ..curriculum.views import QuestionCreateView
from django.http import HttpRequest
from django.test import TransactionTestCase, SimpleTestCase, TestCase
from django.http import HttpRequest
from django.urls import reverse
from ..curriculum import views
import unittest


class HomePageTests(SimpleTestCase):
    @classmethod

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('WMGTSS Dashboard'))
        self.assertEquals(response.status_code, 200)
    
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('WMGTSS Dashboard'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Dashboard')


class TestViews(TestCase):
    """
    Includes tests for all the functionality
    associated with Views
    """
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@swapps.co',
            password='top_secret'
        )
        self.client.login(username='test_user', password='top_secret')
        self.user_two = get_user_model().objects.create_user(
            username='user2', password='top_secret')


class qnapageTests(TransactionTestCase):
    def test_question_create_view(self):
            """
            QuestionCreateView should create a new question object.
            """
            subject = 'This is my question'
            current_question_count = Question.objects.count()
            course = Question.course
            response = self.client.post(
            reverse('curriculum:question_create', 
                kwargs={'course':course.slug,'slug':self.object.slug}),
            {'subject': subject, 'question': 'babla', 'tags': 'test tag'}),
            self.assertEqual(response.status_code, 302)
            new_question = Question.objects.first()
            self.assertEqual(new_question.subject,subject)
            self.assertEqual(Question.objects.count(),
                         current_question_count + 1)

class qnasubject(TransactionTestCase):
    @override_settings(QA_SETTINGS={'question_subject_optional': True})
    def test_create_question_optional_description(self):
            """
            When QUESTION_SUBJECT_OPTIONAL is True, the validation for description
            should be disabled on the form, allowing the object to be created
            without specifying it.
            """
            subject = 'This is my question'
            current_question_count = Question.objects.count()
            response = self.client.post(
                reverse('question_create'),
                {'subject': subject, 'tags': 'test tag'})
            self.assertEqual(response.status_code, 302)
            new_question = Question.objects.last()
            self.assertEqual(new_question.subject, subject)
            self.assertEqual(Question.objects.count(), current_question_count + 1)

    @override_settings(QA_SETTINGS={'question_subject_optional': False})
    def test_create_question_optional_description_false(self):
            """
            When QUESTION_SUBJECT_OPTIONAL is False (default), the validation for
            description will be on place, and a question cannot be created without
            setting some content for it.
            """
            test = Question.objects.create(
            subject='poost',  
            slug='django'
            )
            subject = 'This is my question'
            current_question_count = Question.objects.count()
            response = self.client.post(
                reverse('question_create', args=(test.slug,)),
                {'subject': subject, 'tags': 'test tag'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(Question.objects.count(), current_question_count)