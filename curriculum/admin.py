from django.contrib import admin
from django.contrib import admin
from curriculum.forms import QuestionForm

from curriculum.models import Course, Module, Assignment, Grade, Question, Submission, Standard

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

class QuestionInline(admin.TabularInline):
  model = Question
  show_change_link = True


class QuestionAdmin(admin.ModelAdmin):
  model = Question

class SubmissionAdmin(admin.ModelAdmin):
   model = Submission


admin.site.register(Question, QuestionAdmin)
admin.site.register(Standard)
admin.site.register(Submission, SubmissionAdmin)

