from django.contrib import admin

from .models import Courses, Modules, Assignments, Sessions

admin.site.register(Courses)
admin.site.register(Modules)
admin.site.register(Assignments)
admin.site.register(Sessions)
# Register your models here.
