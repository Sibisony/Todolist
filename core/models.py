from turtle import title
from venv import create
from django.db import models

# Create your models here.
class ToDo(models.Model):
    title=models.CharField(max_length=256)
