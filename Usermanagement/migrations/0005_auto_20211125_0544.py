# Generated by Django 3.2.9 on 2021-11-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usermanagement', '0004_alter_user_mob_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
