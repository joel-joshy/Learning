from django.urls import path
from .views import AddCourseView, AddModuleView


urlpatterns = [
    path('course/<int:pk>', AddCourseView.as_view(), name='add-course'),
    path('course/module/<int:pk>', AddModuleView.as_view(),
         name='add-module')
]
