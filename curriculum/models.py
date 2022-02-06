from tkinter.messagebox import YES
from django.db import models
from django.template.defaultfilters import slugify
import os, datetime
from re import match
from django.contrib.auth.forms import UsernameField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.forms import RadioSelect, widgets

#function to rename the file name when admin upload a picture to a course
#it renames the photo by the course id
def course_rename(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]

    #retreive filename
    if instance.course_id:
        filename = 'Course_Image/{}.{}'.format(instance.course_id, ext)
    return os.path.join(upload_to,filename)

#function to rename the file name when tutors upload lectures slides 
#it renames the lecture by the lecture id 
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

#create a course model 
class Course(models.Model):
    course_id = models.CharField(unique=True, max_length=50) #unique course ids
    name = models.TextField(max_length=50)
    slug = models.SlugField(null=True, blank=True) #slug to create a url link between models
    image = models.ImageField(upload_to=course_rename, blank=True, verbose_name="Course Image") #course image
    description = models.TextField(max_length=500, blank=True)
    
    #course model returns the course name from the function
    def __str__(self):
        return self.name
    
    #the course model slugifies the course name so when a new course is added 
    #its slug becomes the course name 
    #arguments and keyword arguments are saved 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#create a module model 
class Module(models.Model):
    module_id = models.IntegerField(unique=True, max_length=100) #unique module ids
    name = models.TextField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules') #course fk and related names will relate to the CBV
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)  #slug to create a url link between models

    #module model returns the module name from the function
    def __str__(self):
        return self.name
    
    #the module model slugifies the module name so when a new module is added 
    #its slug becomes the module name 
    #arguments and keyword arguments are saved
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#function to rename the file name when tutors upload lessons vidoes or notes
#it renames the lecture by the lecture id 
def save_lesson_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.id:
        filename = 'lecture_files/{}/{}.{}'.format(instance.id,instance.id, ext)
        if os.path.exists(filename):
            new_name = str(instance.id) + str('1')
            filename =  'lecture_images/{}/{}.{}'.format(instance.d,new_name, ext)
    return os.path.join(upload_to, filename)

#create a lecture model 
class Lecture(models.Model):
    id = models.IntegerField(primary_key =True) 
    name = models.TextField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures') #course fk and related names will relate to the CBV
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lectures') #module fk and related names will relate to the CBV
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True) #slug to create a url link between models
    slides = models.FileField(upload_to=save_lecture_slides, verbose_name= "Lecture Slides", blank=True)
    video = models.FileField(upload_to=save_lesson_files,verbose_name="Video", blank=True, null=True)
    notes = models.FileField(upload_to=save_lesson_files,verbose_name="Notes", blank=True)

    #lecture model returns the lecture name from the function
    def __str__(self):
        return self.name
     
    #the lecture model slugifies the lecture name so when a new lecture is added 
    #its slug becomes the lecture name 
    #arguments and keyword arguments are saved
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    #reverse url so you can go back to the questions list page after selecting lectures. 
    #the slug reverses from the selected lecture using key word arguments 
    #the lectures module and course with be in the slug URL
    def get_absolute_url(self):
        return reverse('curriculum:lecture_list', kwargs={'slug':self.module.slug, 'course':self.course.slug})

#create a assignment model 
class Assignment(models.Model):
    id = models.CharField(primary_key =True, max_length=50) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments') #course fk and related names will relate to the CBV
    module = models.ForeignKey(Module, on_delete=models.CASCADE,related_name='assignments') #module fk and related names will relate to the CBV
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=250)
    slug = models.SlugField(null=True, blank=True) #slug to create a url link between models
    duedate = models.DateTimeField()
    
    #assignment model returns the assignment name from the function
    def __str__(self):
        return self.name
    
    #the assignment model slugifies the assignment name so when a new assignment is added 
    #its slug becomes the assignment name 
    #arguments and keyword arguments are saved
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    #reverse url so you can go back to the assignment list page after selecting assignments 
    #the slug reverses from the selected assignment using key word arguments 
    #the assignment, module and course with be in the slug URL
    def get_absolute_url(self):
        return reverse('curriculum:assignment_list', kwargs={'slug':self.module.slug, 'course':self.course.slug})

#function to rename the file name when users upload a question attachement
#it renames the picture by the username who uploads it 
def save_rename_question(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    #retreive filename
    if instance.created_by.username:
        filename = 'Question_Attachment/{}.{}'.format(instance.created_by.username, ext)
    return os.path.join(upload_to,filename)

#create a question model 
class Question(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='questions', default = 1) #module fk and related names will relate to the CBV
    subject = models.CharField(max_length = 100)
    
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
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='questions', null=True) #assignment fk and related names will relate to the CBV
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='questions', null=True) #lecture fk and related names will relate to the CBV
    question = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True) #fk from django custom model user
    now = datetime.datetime.now()
    created_at = models.DateTimeField('date published', default=now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = 1, related_name='questions') #course fk and related names will relate to the CBV
    picture = models.ImageField(upload_to=save_rename_question, verbose_name ="Question Attachment:", blank=True)
    
    Yes = 'Yes'
    No ='No'

    options = [
        (Yes,'Yes'),
        (No ,'No'),
        ]
    anonymous = models.CharField(max_length=5, verbose_name ="Submit Anonymously", choices=options, default=No)
    slug = models.SlugField(null=True, blank=True)

    #order the questions by the most recent questions
    class Meta:
        ordering = ['-created_at']

    #question model returns the question subjectfrom the function
    def __str__(self):
        return self.subject
    
    #the question model slugifies the question subject so when a new question is added 
    #its slug becomes the question subject
    #arguments and keyword arguments are saved
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject)
        super().save(*args, **kwargs)

    #reverse url so you can go back to the question list page after selecting a question 
    #the slug reverses from the selected question using key word arguments 
    #the question, module and course with be in the slug URL
    def get_absolute_url(self):
        return reverse('curriculum:question_list', kwargs={'slug':self.module.slug, 'course':self.course.slug})

#create a answer  model 
class Answer(models.Model):
    question = models.ForeignKey(Question,null=True, on_delete=models.CASCADE,related_name='answers') #question fk and related names will relate to the CBV
    answer = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    #the answer model slugifies the who answered and when 
    #its slug becomes the answer
    #arguments and keyword arguments are saved
    def save(self, *args, **kwargs):
        self.answer= slugify("answered by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    #answer model returns the answer 
    def __str__(self):
        return self.answer

    #order by the most recently answered 
    class Meta:
        ordering = ['-date_added']
