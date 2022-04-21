from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_photo = CloudinaryField('image')
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.phone

    def __str__(self):
        return self.user.username
        
class Semester(models.Model):
    semester_name              =   models.CharField(max_length=100, help_text='Eg-one, two,three etc')
    semester_name_in_numeric   =   models.IntegerField(help_text='Eg- 1,2,4,5 etc') 
    section                 =   models.CharField(max_length=10, help_text='Eg- A,B,C etc')
    creation_date           =   models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('student_semesters:semester_list')

    def __str__(self):
        return "%s Section-%s"%(self.class_name, self.section)

class Student(models.Model):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    email = models.EmailField()
    gender = models.CharField(max_length=8, choices=select_gender)
    student_class = models.ForeignKey(Semester, on_delete=models.CASCADE)
    dob= models.DateField(default=date.today())
    regno = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('students:student_create')

    def __str__(self):
        return self.name


class Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_code = models.IntegerField()
    unit_creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    unit_update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.unit_name
    
    def get_absolute_url(self):
        return reverse('units:unit_list')



