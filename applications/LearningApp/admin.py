from django.contrib import admin
from .models import Modules,Course,Quiz,Questions,Choices
# Register your models here.

admin.site.register(Course)
admin.site.register(Modules)
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Choices)
