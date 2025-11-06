from django.db import models


class Student(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  Department = models.CharField(max_length=255)
  datecreated = models.DateTimeField(auto_now_add=True)

# Create your models here.
  def __str__(self):
     return f"{self.firstname} {self.lastname}"
    