from django.db import models
from django.template.defaultfilters import slugify
import os, datetime
from re import match
from django.contrib.auth.forms import UsernameField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

def course_rename(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]

    #retreive filename
    if instance.course_id:
        filename = 'Course_Image/{}.{}'.format(instance.course_id, ext)
    return os.path.join(upload_to,filename)

def save_lecture_slides(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]

    #retreive filename
    if instance.lecture_id:
        filename = 'Lecture_Slides/{}.{}'.format(instance.lecture_id,instance.lecture_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.lecture_id) + str('1')
            filename = 'Lecture_Slides/{}.{}'.format(instance.lecture_id,new_name, ext)
    return os.path.join(upload_to,filename)
    
class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Course(models.Model):
    course_id = models.CharField(primary_key =True, max_length=50) 
    course_name = models.TextField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='courses')
    image = models.ImageField(upload_to=course_rename, blank=True, verbose_name="Course Image")
    course_description = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.course_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_id)
        super().save(*args, **kwargs)

class Module(models.Model):
    module_id = models.IntegerField(primary_key =True) 
    module_name = models.TextField(max_length=50)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.module_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.module_name)
        super().save(*args, **kwargs)

class Lecture(models.Model):
    lecture_id = models.IntegerField(primary_key =True) 
    lecture_title = models.TextField(max_length=50)
    module_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
    slug = models.SlugField(null=True, blank=True)
    slides = models.FileField(upload_to=save_lecture_slides, verbose_name= "Lecture Slides", blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.lecture_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lecture_title)
        super().save(*args, **kwargs)
    
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


