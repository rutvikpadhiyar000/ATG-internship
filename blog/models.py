from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import CharField
# Create your models here.

class BlogPost(models.Model):
   
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField()
    catagory = CharField(max_length=20)
    summary = models.CharField(max_length=500)
    content = models.TextField()