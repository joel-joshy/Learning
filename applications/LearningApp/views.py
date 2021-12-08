from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AddCourseSerializer, AddModuleSerializer , \
    AddQuizSerializer
from .models import Course, Modules, Quiz
from .permissions import IsOwner

from applications.Usermanagement.models import User


class AddCourseView(generics.RetrieveUpdateDestroyAPIView,
                    generics.CreateAPIView):

    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = AddCourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)


class AddModuleView(generics.CreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddModuleSerializer
    queryset = Modules.objects.all()


class AddQuizView(generics.CreateAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddQuizSerializer
    queryset = Quiz.objects.all()

