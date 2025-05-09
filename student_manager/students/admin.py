from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Address , Student2,Address2, StudentProfile

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'postal_code', 'country')
    search_fields = ('street', 'city', 'state', 'postal_code')


@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('addresses',)

@admin.register(Address2)
class Address2Admin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'postal_code', 'country')
    search_fields = ('street', 'city', 'state', 'postal_code')



@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'graduation_year')
    list_filter = ('graduation_year',)
    search_fields = ('student__first_name', 'student__last_name', 'bio')
    readonly_fields = ('display_profile_picture',)
    
    def display_profile_picture(self, obj):
        if obj.profile_picture:
            return f'<img src="{obj.profile_picture.url}" width="150" height="150" />'
        return "No image"
    
    display_profile_picture.allow_tags = True
    display_profile_picture.short_description = 'Profile Picture Preview'