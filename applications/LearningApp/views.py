from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AddCourseSerializer, AddModuleSerializer
from .models import Course, Modules

from applications.Usermanagement.models import User


class AddCourseView(generics.RetrieveUpdateDestroyAPIView,
                    generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = AddCourseSerializer
    queryset = Course.objects.all()


class AddModuleView(generics.CreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddModuleSerializer
    queryset = Modules.objects.all()
