from django.contrib import admin

from .models import User, Institution, SubDomain

# Register your models here.


class CustomAdmin(admin.ModelAdmin):

    list_display = [
        'email', 'id','first_name', 'last_name', 'username', 'role',
        'institution', 'employee_id', 'is_verified', 'created'
    ]

    fields = [
        'username', 'password', 'first_name', 'last_name', 'email', 'employee_id', 'mob_number', 'role', 'dob', 'institution', 'is_verified',
        'is_active', 'is_superuser', 'is_staff'
    ]

    list_filter = [
          'role', 'institution', 'is_active', 'is_verified', 'is_superuser'
    ]
    search_fields = ['username', 'first_name', 'last_name', 'email', 'role', 'institution__institution_name',
                     'mob_number', 'employee_id']


class InstitutionAdmin(admin.ModelAdmin):

    list_display = ['institution_name', 'id', 'created_by', 'is_active']
    fields = ['institution_name', 'created_by', 'logo', 'address', 'is_active']
    search_fields = ['institution_name', 'created_by__email']
    list_filter = ['created_by', 'is_active']


class SubDomainAdmin(admin.ModelAdmin):

    list_display = ['domain_name', 'id', 'institution']
    fields = ['domain_name', 'institution']
    search_fields = ['institution__institution_name', 'domain_name']


admin.site.register(User, CustomAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(SubDomain, SubDomainAdmin)
