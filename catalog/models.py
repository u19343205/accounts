from re import match
from django.contrib.auth.forms import UsernameField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
import os 
import datetime
import time
from datetime import timedelta

from django.utils.translation import deactivate_all


#function to define the renaming of images when users upload a picture to their question submission to WMGTSS
def save_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]

    #retreive filename
    if instance.user.username:
        filename = 'Profile_Picture/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to,filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(upload_to=save_rename, verbose_name ="Profile Picture", blank=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    id = models.CharField(primary_key =True, max_length=50) 
    name = models.TextField(max_length=50)
    #lead = models.OneToOneField(User, on_delete=models.CASCADE)


class Module(models.Model):
    id = models.IntegerField(primary_key =True) 
    name = models.TextField(max_length=50)
    course= models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    
class Assignment(models.Model):
    id = models.CharField(primary_key =True, max_length=50) 
    name = models.TextField()
    course= models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=1)
    duedate = models.DateTimeField()
    
class Grade(models.Model):
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=1)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default=1)

def save_rename_question(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]

    #retreive filename
    if instance.user.username:
        filename = 'Question_Attachment/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to,filename)

class Question(models.Model):
    
    #module = models.OneToOneField(Module, on_delete=models.CASCADE, default=0)
    Assignment_Related = 'Assignment Related'
    Lecture_Related = 'Lecture Related'
    General = 'General'

    topics = [

    (Assignment_Related,'Assignment Related'),
    (Lecture_Related,  'Lecture Related'),
    (General, 'General'),
    ]
    
    topics = models.CharField(max_length=20, choices=topics, default=General)
    subject = models.TextField(max_length = 100, null=True)
    question = models.TextField()
    now = datetime.datetime.now()
    pub_date = models.DateTimeField('date published', default=now)
    picture = models.ImageField(upload_to=save_rename_question, verbose_name ="Question Attachment", blank=True)
    ordering = ['-date']


    def __str__(self):
        return self.subject


class Submission(models.Model):
  submission = models.ForeignKey(Question, on_delete=models.PROTECT)
  email = models.EmailField(max_length=100)
  status = models.CharField(max_length=255)

class Student(models.Model):
    student_name = models.CharField(max_length=200)