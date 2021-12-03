# Generated by Django 3.2.9 on 2021-12-02 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningApp', '0003_auto_20211201_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='duration',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Module Duration'),
        ),
        migrations.AlterField(
            model_name='choices',
            name='choice',
            field=models.CharField(max_length=200, verbose_name='Choice'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=250, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_name',
            field=models.CharField(max_length=200, verbose_name='Quiz Name'),
        ),
    ]