
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Music(models.Model):
    
    course_name=models.CharField(max_length=100,blank=True, null=True)
    student_name=models.CharField(max_length=100,blank=True, null=True)
    teachername=models.CharField(max_length=100,blank=True, null=True)
    genres=models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.course_name
    
class Student_Details(models.Model):
    full_name=models.CharField(max_length=100,blank=True, null=True)
    address=models.CharField(max_length=100,blank=True, null=True)
    phone_no=models.IntegerField(10,blank=True, null=True)
    
    
    
    def __str__(self):
        return self.full_name
    