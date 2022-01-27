from django.contrib import admin
from django.contrib import admin
from curriculum.forms import QuestionForm

from curriculum.models import Course, Module, Question

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass

class QuestionInline(admin.TabularInline):
  model = Question
  show_change_link = True


class QuestionAdmin(admin.ModelAdmin):
  model = Question


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Standard)


