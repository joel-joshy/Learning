from rest_framework import serializers

from .models import Course, Modules, Quiz, Questions, Choices


class AddCourseSerializer(serializers.ModelSerializer):
    """
    serializer to add course
    """
    class Meta:
        model = Course
        fields = [
            'course_name', 'course_details', 'course_duration',

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
            'quiz_name', 'quiz_details', 'module',
            'pass_mark'
        ]


class AddQuestionChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choices
        fields = [
            'id', 'choice', 'answer'
        ]


class AddQuestionSerializer(serializers.ModelSerializer):
    choices = AddQuestionChoiceSerializer(
        many=True, read_only=True, source='get_choices'
    )
    right_answer = serializers.SerializerMethodField()

    class Meta:
        model = Questions
        fields = [
            'quiz', 'question', 'choices', 'right_answer'
        ]

    def get_right_answer(self, obj):
        right_answer = obj.get_choices.filter(
            answer=True
        ).first()
        return right_answer.choice if right_answer else None