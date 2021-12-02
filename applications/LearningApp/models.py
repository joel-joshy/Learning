from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from applications.Usermanagement.models import User
from common.abstract_models import DateBaseModel
# Create your models here.


class Course(DateBaseModel, models.Model):

    course_name = models.CharField(verbose_name="Course Name", max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_courses', verbose_name='Created By')
    course_details = models.TextField()
    course_duration = models.FloatField()
    students = models.ManyToManyField(User, through='StudentCourseStats', blank=True,
                                      verbose_name='Students', related_name='courses')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ('-created',)


class StudentCourseStats(DateBaseModel, models.Model):

    COMPLETED = 'completed'
    IN_PROGRESS = 'in_progress'
    NEW = 'new'

    STATUS_CHOICES = (
        (COMPLETED, 'Completed'),
        (IN_PROGRESS, 'In Progress'),
        (NEW, 'New')

    )

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,
                             related_name='get_student_course_stats')
    course = models.ForeignKey(Course, verbose_name='Course', on_delete=models.CASCADE,
                               related_name='get_student_course_stats')
    completion_percentage = models.FloatField('Completion Percentage', validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
                                              default=0.0)
    status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES, default=IN_PROGRESS)

    class Meta:

        verbose_name = "Student Course Stats"
        verbose_name_plural = "Student Course Stats"
        ordering = ('-created',)
        unique_together = ('user', 'course')

    def __str__(self):
        return '%s - %s' % (self.user, self.course)


class Modules(DateBaseModel, models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='get_modules')
    module_name = models.CharField(verbose_name='Module Name', max_length=200)
    module_details = models.TextField()

    files = models.FileField(upload_to='images', null=True, blank=True)
    students = models.ManyToManyField(User, related_name='get_modules', blank=True)

    def __str__(self):
        return str(self.module_name) + ' - ' + str(self.course.course_name)

    class Meta:
        verbose_name = "Course Module"
        verbose_name_plural = "Course Modules"
        ordering = ('-created',)


class Quiz(DateBaseModel, models.Model):

    quiz_name = models.CharField(verbose_name="Quiz", max_length=200)
    quiz_details = models.TextField()
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_quizzes')
    pass_mark = models.IntegerField()
    students_attended = models.ManyToManyField(User, related_name='quizzes', blank=True)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ('-created',)

    def __str__(self):
        return self.quiz_name


class Questions(DateBaseModel, models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(verbose_name="Question", max_length=250)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ('-created',)

    def __str__(self):
        return self.question


class Choices(DateBaseModel, models.Model):

    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(verbose_name="Choice", max_length=200)
    answer = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Module Test Question Choice"
        verbose_name_plural = "Module Test Question Choice"
        ordering = ('-created',)

    def __str__(self):
        return self.question.question