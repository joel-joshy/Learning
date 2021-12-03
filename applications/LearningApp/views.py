from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AddCourseSerializer
from .models import Course

from applications.Usermanagement.models import User

# Create your views here.


class AddCourseView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = AddCourseSerializer
    search_fields = ['course_name', 'created_by__email']
    queryset = Course.objects.all()



