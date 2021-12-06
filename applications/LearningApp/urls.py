from django.urls import path
from .views import AddCourseView


urlpatterns = [
    path('course', AddCourseView.as_view(), name='add-course')
]
