from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, default="")
    bloggers_name = models.CharField(max_length=100, default="")