from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Modules, Course, Quiz, Questions, Choices, StudentCourseStats

# Register your models here.


class CourseModuleInline(StackedInline):
    model = Modules
    extra = 0
    verbose_name = "Course Module"
    verbose_name_plural = "Course Modules"


class ModuleTestQuestionsInline(StackedInline):
    model = Quiz
    extra = 0
    verbose_name = "Module Test Question"
    verbose_name_plural = "Module Test Questions"


class CourseAdmin(admin.ModelAdmin):

    list_display = [
        'course_name', 'created_by', 'course_duration'
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
        'module_name', 'course',
    ]
    fields = [
        'module_name', 'course', 'module_details', 'files', 'students'
    ]

    search_fields = [
        'module_name', 'course__course_name', 'students__email'
    ]
    list_filter = [
        'course__created_by__institution'
    ]
    inlines = [ModuleTestQuestionsInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Modules, CourseModuleAdmin)
admin.site.register(StudentCourseStats)

admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Choices)
