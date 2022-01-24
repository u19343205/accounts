from django.contrib import admin

from catalog.models import  Profile, Course, Module, Assignment, Grade, Question, Choice, Submission

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

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

class ChoiceInline(admin.TabularInline):
  model = Choice

class QuestionAdmin(admin.ModelAdmin):
  inlines = [
    ChoiceInline
  ]
class SubmissionAdmin(admin.ModelAdmin):
   model = Submission


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)