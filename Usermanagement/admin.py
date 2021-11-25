from django.contrib import admin
from .models import User,Institution,SubDomain
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    fields = [
        'username','password','first_name','last_name','email','mob_number','role','dob','institution','is_verified',
        'is_active','is_superuser','is_staff'
    ]

    list_display = [
        'username','email','role'
    ]
    list_filter = [
        'is_staff','is_superuser'
    ]
class UserAdminCustom(UserAdmin):
    list_display = ('username','email','role')
    list_filter = ('is_superuser','is_staff')
    search_fields = ('username',)
    fieldsets = (
        (None, {'fields': ('email','username', 'password','role')}),
        ('Personal info', {'fields': ('first_name','last_name','dob','mob_number','institution')}),
        ('Permissions', {'fields': ('is_verified','is_active','is_superuser','is_staff')}),
    )


admin.site.register(User,CustomAdmin)

admin.site.register(Institution)
admin.site.register(SubDomain)