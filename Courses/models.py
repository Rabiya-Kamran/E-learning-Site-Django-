from django.db import models

# Create your models here.
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, null=True, blank=True)  # Allow description to be null

    def __str__(self):
        return self.title
    

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    # renames the objects of the model
    # with their title name
    def __str__(self):
        return self.title