# Generated by Django 3.2.9 on 2021-11-25 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usermanagement', '0003_user_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mob_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]