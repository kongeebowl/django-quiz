from rest_framework import serializers
from .models import User



from .models import Question, User,Choices


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