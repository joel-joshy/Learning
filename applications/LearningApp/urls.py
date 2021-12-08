from django.urls import path
from .views import AddCourseView, AddModuleView, AddQuizView


urlpatterns = [
    path('course/<int:pk>', AddCourseView.as_view(), name='add-course'),
    path('course/module/<int:pk>', AddModuleView.as_view(),
         name='add-module'),
    path('course/module/quiz/<int:pk>', AddQuizView.as_view(),
         name='add-quiz')
]
