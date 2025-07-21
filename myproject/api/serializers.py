from rest_framework import serializers
from .models import User
import random
from .models import Question, User, Quiz


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['answer']

class QuizSerializer(serializers.ModelSerializer):

    questions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Question.objects.all(),
        required=False,   
        allow_empty=True    
    )
    
    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)

        all_questions = list(Question.objects.all())
        num_questions = min(10, len(all_questions))
        random_questions = random.sample(all_questions, num_questions)

    
        instance.questions.clear()
        instance.questions.add(*random_questions)

        return instance

    class Meta:
        model = Quiz
        fields = '__all__'