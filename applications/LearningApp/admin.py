from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Modules, Course, Quiz, Questions, Choices, StudentCourseStats

# Register your models here.


class CourseModuleInline(StackedInline):
    model = Modules
    extra = 0
    verbose_name = "Course Module"
    verbose_name_plural = "Course Modules"


class ModuleTestQuizInline(StackedInline):
    model = Quiz
    extra = 0
    verbose_name = "Module Test Question"
    verbose_name_plural = "Module Test Questions"


class QuizQuestionsInline(StackedInline):
    model = Questions
    extra = 0
    verbose_name = "Test Quiz Question"
    verbose_name_plural = "Test Question Quizzes"


class QuestionChoiceInline(StackedInline):
    model = Choices
    extra = 0
    verbose_name = "Question Choice"
    verbose_name_plural = "Question Choices"


class CourseAdmin(admin.ModelAdmin):

    list_display = [
         'course_name', 'created_by', 'id', 'course_duration'
    ]
    fields = [
        'course_name', 'created_by', 'course_details',
        'course_duration'
    ]
    search_fields = [
        'course_name', 'created_by__email', 'course_details',
        'course_duration'
    ]

    list_filter = ['course_name']
    inlines = [CourseModuleInline]


class CourseModuleAdmin(admin.ModelAdmin):

    list_display = [
        'module_name', 'id', 'course',
    ]
    fields = [
        'module_name', 'course', 'module_details', 'files', 'duration', 'students'
    ]

    search_fields = [
        'module_name', 'course__course_name', 'students__email'
    ]
    list_filter = [
        'course__created_by__institution'
    ]
    inlines = [ModuleTestQuizInline]


class QuizAdmin(admin.ModelAdmin):

    list_display = [
        'quiz_name', 'id', 'created_by', 'pass_mark'
    ]
    fields = [
        'quiz_name', 'quiz_details', 'module','created_by',
        'pass_mark'
    ]
    list_filter = [
        'created_by'
    ]
    inlines = [QuizQuestionsInline]


class QuestionAdmin(admin.ModelAdmin):

    list_display = [
        'question', 'id', 'quiz'
    ]
    fields = [
        'question', 'quiz'
    ]

    search_fields = [
        'question', 'quiz__quiz_name'
    ]
    list_filter = [
        'quiz'
    ]
    inlines = [QuestionChoiceInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Modules, CourseModuleAdmin)
admin.site.register(StudentCourseStats)

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Questions,QuestionAdmin)
admin.site.register(Choices)
