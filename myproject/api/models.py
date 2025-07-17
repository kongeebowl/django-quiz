from django.db import models
import random


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.username





class Question(models.Model):
    question_text = models.CharField(max_length=200)


    def __str__(self):
        return self.question_text


class Choices(models.Model):
    choice_text = models.CharField(max_length=150)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', null=True, blank=True)
    

    def __str__(self):
        return self.choice_text

class Quiz(models.Model):
    description = models.CharField(max_length=255)
    quiz_number = models.IntegerField(default=0, unique=True)
    questions = models.ManyToManyField(Question, related_name='quizzes')    


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


        all_questions = list(Question.objects.all())


        num_questions = min(10, len(all_questions))
        random_questions = random.sample(all_questions, num_questions)


        self.questions.clear()
        self.questions.add(*random_questions)


    def __str__(self):
        return self.description



