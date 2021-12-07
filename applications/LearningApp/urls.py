from django.urls import path
from .views import AddCourseView


urlpatterns = [
    path('course/<int:pk>', AddCourseView.as_view(), name='add-course')
]
