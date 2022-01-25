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
