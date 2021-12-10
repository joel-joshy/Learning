from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from .serializers import AddCourseSerializer, AddModuleSerializer, \
    AddQuizSerializer, AddQuestionSerializer, ViewQuestionSerializer, \
    AddQuestionChoiceSerializer

from .models import Course, Modules, Quiz, Questions, Choices
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
        try:
            return self.queryset.filter(created_by=self.request.user)
        except:
            pass


class AddModuleView(generics.CreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddModuleSerializer
    queryset = Modules.objects.all()


class AddQuizView(generics.CreateAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = AddQuizSerializer
    queryset = Quiz.objects.all()

    def perform_update(self, serializer):
        return serializer.save(created_by=self.request.user)


class AddQuestionView(generics.ListCreateAPIView):

    serializer_class = AddQuestionSerializer
    queryset = Questions.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AddQuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class ListQuestionView(generics.ListAPIView):

    serializer_class = ViewQuestionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Questions.objects.all()


class AddChoiceView(generics.CreateAPIView,
                    generics.UpdateAPIView):
    serializer_class = AddQuestionChoiceSerializer
    queryset = Choices.objects.all()
