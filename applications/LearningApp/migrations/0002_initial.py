# Generated by Django 3.2.9 on 2021-12-01 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LearningApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcoursestats',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_student_course_stats', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_quizzes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quiz',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningApp.modules'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='students_attended',
            field=models.ManyToManyField(blank=True, related_name='quizzes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningApp.quiz'),
        ),
        migrations.AddField(
            model_name='modules',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_modules', to='LearningApp.course'),
        ),
        migrations.AddField(
            model_name='modules',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='get_modules', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_courses', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses', through='LearningApp.StudentCourseStats', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
        migrations.AddField(
            model_name='choices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningApp.questions'),
        ),
        migrations.AlterUniqueTogether(
            name='studentcoursestats',
            unique_together={('user', 'course')},
        ),
    ]
