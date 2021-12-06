from rest_framework import serializers

from .models import Course, Modules


class AddCourseSerializer(serializers.ModelSerializer):
    """
    serializer to add course
    """
    class Meta:
        model = Course
        fields = [
            'course_name', 'created_by', 'course_details', 'course_duration'
        ]


