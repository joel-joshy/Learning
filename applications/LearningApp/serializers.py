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
            'id', 'question', 'choice', 'answer'
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


class ViewQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = [
            'quiz', 'id', 'question'
        ]


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choices
        fields = [
            'question', 'choice', 'answer'
        ]


class QuestionSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True, source='get_choices',
                               required=False)
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


class QuizSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True, source='get_questions')
    # created_by = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = [
            'quiz_name', 'quiz_details', 'module',
            'pass_mark',
            'questions',
        ]


class ModuleSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(many=True, source='get_quizzes')

    class Meta:
        model = Modules
        fields = [
            'course', 'module_name', 'module_details', 'duration', 'files',
            'quiz'
        ]



