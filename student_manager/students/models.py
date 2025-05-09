from django.db import models
import os

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



# New models for many-to-many relationship
class Address2(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}"

class Student2(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    addresses = models.ManyToManyField(Address2, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



def student_profile_picture_path(instance, filename):
 # File will be uploaded to MEDIA_ROOT/student_profile_pictures/<student_id>/<filename>
    return os.path.join('student_profile_pictures', str(instance.student.id), filename)

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=student_profile_picture_path, blank=True, null=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"Profile for {self.student}"
