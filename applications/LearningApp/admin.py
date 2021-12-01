from django.contrib import admin
from .models import Modules, Course, Quiz, Questions, Choices, StudentCourseStats
# Register your models here.

admin.site.register(Course)
admin.site.register(Modules)
admin.site.register(StudentCourseStats)

admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Choices)
