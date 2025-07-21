from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.question_text


class Quiz(models.Model):
    description = models.CharField(max_length=255)
    quiz_number = models.IntegerField(default=0, unique=True)
    questions = models.ManyToManyField(Question, related_name='quizzes')    

    def __str__(self):
        return self.description
