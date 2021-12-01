from django.db import models

from applications.Usermanagement.models import User
# Create your models here.


class Course(models.Model):

    course_name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_courses')
    course_details = models.TextField()
    course_duration = models.IntegerField()
    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.course_name


class Modules(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='get_modules')
    module_name = models.CharField(max_length=200)
    module_details = models.TextField()

    files = models.FileField(upload_to='images', null=True, blank=True)
    students = models.ManyToManyField(User, related_name='get_modules', blank=True)

    def __str__(self):
        return self.module_name


class Quiz(models.Model):

    quiz_name = models.CharField(max_length=200)
    quiz_details = models.TextField()
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_quizzes')
    pass_mark = models.IntegerField()
    students_attended = models.ManyToManyField(User, related_name='quizzes', blank=True)

    def __str__(self):
        return self.quiz_name


class Questions(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.question


class Choices(models.Model):

    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.question.question