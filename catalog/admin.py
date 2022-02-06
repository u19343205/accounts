from django.contrib import admin 
from catalog.models import Profile
#register the profile model onto the admin site 
admin.site.register(Profile)