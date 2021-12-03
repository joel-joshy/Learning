from django.urls import path
from .views import AddCourseView



urlpatterns = [
    path('course', AddCourseView, name='add-course')
]
