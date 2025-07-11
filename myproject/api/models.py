
# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.username

class Choices(models.Model):
    choice_text = models.CharField(max_length=150, unique=True)
    choice_number = models.IntegerField(default=0, unique=True)
    def __str__(self):
        return self.choice_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Quiz(models.Model):
    description = models.CharField(max_length=255)
    quiz_number = models.IntegerField(default=0, unique=True)
    question = models.ForeignKey(Question, default=1, on_delete=models.CASCADE, related_name='questions')
    def __str__(self):
        return self.description

        







