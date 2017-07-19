from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class CourseManager(models.Manager):
#     def add(self, postData):
#         print "Adding book to database"
#         course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
#         return course


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at =models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    #objects = CourseManager()
