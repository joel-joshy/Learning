from rest_framework import serializers

from .models import Course, Modules, Quiz


class AddCourseSerializer(serializers.ModelSerializer):
    """
    serializer to add course
    """
    class Meta:
        model = Course
        fields = [
            'course_name', 'course_details', 'course_duration'
        ]


class AddModuleSerializer(serializers.ModelSerializer):

    """
    serializer to add module
    """
    class Meta:
        model = Modules
        fields = [
            'course', 'module_name', 'module_details', 'duration', 'files'
        ]


class AddQuizSerializer(serializers.ModelSerializer):

    class Meta:

        model = Quiz
        fields = [
            'quiz_name', 'quiz_details', 'module', 'created_by',
            'pass_mark'
        ]
