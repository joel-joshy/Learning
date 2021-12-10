from django.urls import path, include
from .views import AddCourseView, AddModuleView, AddQuizView, \
    AddQuestionView, ListQuestionView, AddChoiceView, QuestionView, \
    ChoiceView, QuizView, ModuleView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'questions',
                QuestionView)
router.register(r'choices', ChoiceView)
router.register(r'quiz', QuizView)
router.register(r'Module', ModuleView)

urlpatterns = [
    path('course/<int:pk>', AddCourseView.as_view(), name='add-course'),
    path('course/module/<int:pk>', AddModuleView.as_view(),
         name='add-module'),
    path('course/module/quiz/<int:pk>', AddQuizView.as_view(),
         name='add-quiz'),
    path('course/module/quiz/question', AddQuestionView.as_view(),
         name='questions'),
    path('course/module/quiz/questions', ListQuestionView.as_view(),
         name='list-questions'),
    path('quiz/question/choice', AddChoiceView.as_view(),
         name='add-choice'),
    path('', include(router.urls))

]
