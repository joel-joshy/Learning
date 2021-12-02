# Generated by Django 3.2.9 on 2021-12-01 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('institution_name', models.CharField(max_length=200, verbose_name='Institution Name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('mob_number', models.CharField(blank=True, max_length=10, null=True)),
                ('role', models.CharField(blank=True, choices=[('admin', 'Admin'), ('manager', 'Manager'), ('student', 'Student')], default='manager', max_length=20, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Employee ID')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_user', to='Usermanagement.institution', verbose_name='Institution')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Uer Details',
                'verbose_name_plural': 'User Details',
                'ordering': ('-created',),
                'unique_together': {('username',)},
            },
        ),
        migrations.CreateModel(
            name='SubDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('domain_name', models.CharField(max_length=100, unique=True, verbose_name='Domain Name')),
                ('institution', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_domain', to='Usermanagement.institution')),
            ],
            options={
                'verbose_name': 'SubDomain',
                'verbose_name_plural': 'SubDomains',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='institution',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institutions', to=settings.AUTH_USER_MODEL),
        ),
    ]