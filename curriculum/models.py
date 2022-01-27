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
'''  
class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
 '''  

class Course(models.Model):
    course_id = models.CharField(unique=True, max_length=50) 
    name = models.TextField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to=course_rename, blank=True, verbose_name="Course Image")
    description = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Module(models.Model):
    module_id = models.IntegerField(unique=True, max_length=100) 
    name = models.TextField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
'''
class Lecture(models.Model):
    lecture_id = models.IntegerField(primary_key =True) 
    lecture_title = models.TextField(max_length=50)
    module_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = 1)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    slides = models.FileField(upload_to=save_lecture_slides, verbose_name= "Lecture Slides", blank=True)

    def __str__(self):
        return self.lecture_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lecture_title)
        super().save(*args, **kwargs)
    
class Assignment(models.Model):
    id = models.CharField(primary_key =True, max_length=50) 
    name = models.TextField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='assignments', default = 1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments', default = 1)
    duedate = models.DateTimeField()
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
'''
def save_rename_question(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]

    #retreive filename
    if instance.created_by.username:
        filename = 'Question_Attachment/{}.{}'.format(instance.created_by.username, ext)
    return os.path.join(upload_to,filename)

class Question(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='questions', default = 1)
    subject = models.TextField(max_length = 100, default='WMGTSS Question')
    
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
    #assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='question', null=True, )
    #lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='question', null=True)
    question = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    now = datetime.datetime.now()
    created_at = models.DateTimeField('date published', default=now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = 1, related_name='questions')
    picture = models.ImageField(upload_to=save_rename_question, verbose_name ="Question Attachment", blank=True)
    ordering = ['-date']

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject)
        super().save(*args, **kwargs)





class Comment(models.Model):
    question = models.ForeignKey(Question,null=True, on_delete=models.CASCADE,related_name='comments')
    comm_name = models.CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']

class Answer(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
    answer_body = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to " + str(self.comment_name.comm_name)