from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer



from .models import Question, User,Choices, Quiz
from .serializers import QuestionSerializer, UserSerializer,ChoicesSerializer,QuizSerializer

class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AwesomeQuestionView(APIView):
    def get(self, request, pk):
        questions = Question.objects.filter(pk=pk)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  

class ChoicesView(APIView):
    def get(self, request):
        users = Choices.objects.all()
        serializer = ChoicesSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChoicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  


class QuizView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AwesomeQuizView(APIView):
    def get(self, request, pk):
        quizzes = Quiz.objects.filter(pk=pk)
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)