from rest_framework import serializers
from .models import User






from .models import Question, User,Choices, Quiz




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):


    questions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Question.objects.all(),
        required=False,  
        allow_empty=True    
    )
   
    class Meta:
        model = Quiz
        fields = '__all__'

