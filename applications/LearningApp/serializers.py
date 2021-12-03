from rest_framework import serializers

from .models import Course, Modules


class AddCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            'course_name', 'created_by', 'course_details', 'course_duration'
        ]
