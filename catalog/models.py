from re import match
from django.contrib.auth.forms import UsernameField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
import os 
import datetime
import time
from datetime import timedelta


#function to define the renaming of images when users upload a profile picture to WMGTSS
def rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]

    #retreive filename
    if instance.user.username:
        filename = 'Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to,filename)


class Course(models.Model):
    id = models.IntegerField(primary_key =True) 
    name = models.TextField()
    lead = models.TextField()


class Module(models.Model):
    id = models.IntegerField(primary_key =True) 
    name = models.TextField()
    tutor = models.TextField(default=0)
    course= models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    
class Assignment(models.Model):
    id = models.IntegerField(primary_key =True) 
    name = models.TextField()
    course= models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=1)
    duedate = models.DateTimeField()
    

class Grade(models.Model):
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=1)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default=1)

class Question(models.Model):
    Assignment_Related = 'Assignment Related'
    Lecture_Related = 'Lecture Related'
    General = 'General'

    topics = [

    (Assignment_Related,'Assignment Related'),
    (Lecture_Related,  'Lecture Related'),
    (General, 'General'),
    ]
    
    topics = models.CharField(max_length=20, choices=topics, default=General)
    question = models.TextField()

    
    