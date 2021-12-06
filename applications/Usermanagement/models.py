from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import RefreshToken

from common.abstract_models import DateBaseModel


class CustomUserModel(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, DateBaseModel):
    ADMIN = 'admin'
    MANAGER = 'manager'
    STUDENT = 'student'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (STUDENT, 'Student')
    )

    first_name = models.CharField(verbose_name=_('First Name'), max_length=100)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=100)
    username = models.CharField(verbose_name=_("Username"), max_length=20,
                                unique=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    mob_number = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(choices=ROLE_CHOICES, default='manager', max_length=20,
                            blank=True, null=True)
    employee_id = models.CharField(_('Employee ID'), max_length=50, blank=True,
                                   null=True)
    dob = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, related_name='get_user',
                                    verbose_name="Institution", null=True)
    is_verified = models.BooleanField(_('Verified'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserModel()

    class Meta:
        verbose_name = "Uer Details"
        verbose_name_plural = "User Details"
        ordering = ('-created',)
        unique_together = ['username']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Institution(DateBaseModel):
    institution_name = models.CharField(verbose_name=_("Institution Name"),
                                        max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   related_name='institutions', null=True)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    address = models.TextField()
    is_active = models.BooleanField(_('Is Active'), default=True)

    def __str__(self):
        return self.institution_name

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ('-created',)


class SubDomain(DateBaseModel):
    domain_name = models.CharField(verbose_name=_("Domain Name"), max_length=100,
                                   unique=True)
    institution = models.OneToOneField(Institution, on_delete=models.CASCADE,
                                       related_name='sub_domain', null=True)

    def __str__(self):
        return self.domain_name

    class Meta:
        verbose_name = "SubDomain"
        verbose_name_plural = "SubDomains"
        ordering = ('-created',)
