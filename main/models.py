from email.mime import image
from turtle import title
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) # длина заголовка
    description = models.CharField(max_length=250)
    image = models.ImageField()
    url = models.URLField(blank=True)