from datetime import datetime

# Create your models here.
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.username

class Choices(models.Model):
    choice_text = models.CharField(max_length=150, unique=True)
    choice_number = models.IntegerField()
    







