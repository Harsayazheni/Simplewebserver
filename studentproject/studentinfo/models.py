from django.db import models
from django.contrib import admin
# Create your models here.
class student(models,Model):
    referencenumber = models.Charfield(max_length=8)
    name =models.Charfield(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

class StudentAdmin(admin.Model)
    list_display = ('referencenumber','name,'age','email')