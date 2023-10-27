from django.db import models
from django.contrib import admin
# Create your models here.
class ig(models.Model):
    class Meta():
        permissions = (('view_reels',"can view number of reels"),
                       ('view_username',"can access username"),
        )
    username = models.CharField(max_length=100,primary_key=True)
    name =models.CharField(max_length=100)
    posts = models.IntegerField()
    email = models.EmailField()
    privacy = models.CharField(max_length=10)

class igAdmin(admin.ModelAdmin):
    list_display = ('username','name','posts','email','privacy')