from django.test import TestCase
from django.template.defaultfilters import slugify
from curriculum.models import Question, User

#check to ensure when a question is submitted the slug of the question is indeed to subject 
class ModelsTestCase(TestCase):
    def test_question_has_slug(self):
        """Questions are given slugs correctly when saving"""
        question = Question.objects.create(Subject="Ask a Question")
        question.author = "John Doe"
        question.save()
        self.assertEqual(question.slug, slugify(question.subject))

#checks the functionality of submitting a question
class QuestionsModelTestcase(TestCase):
    """Check if creating a question works"""
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(subject="SDLC", question="Is this working?")

    def test_string_method(self):
        """Check that the posted question displays the username"""
        user = Question.objects.get(id=1)
        expected_string = f"Created by: {user.username}"
        self.assertEqual(str(user), expected_string)