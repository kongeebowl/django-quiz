from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer



from .models import Question, User, Quiz
from .serializers import QuestionSerializer, UserSerializer,QuizSerializer, AnswerSerializer

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

class QuestionViewById(APIView):
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

class QuizViewById(APIView):
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

class CheckQuiz(APIView):
    def post(self, request, pk):
        question = Question.objects.get(pk=pk)
        
        answer = AnswerSerializer(question)
        user_answer = request.data.get("user_answer", "")

        correct_answer = question.answer.strip().lower()
        submitted_answer = user_answer.strip().lower()

        is_correct = submitted_answer == correct_answer

        return Response({
            "correct": is_correct,
            "message": "Correct!" if is_correct else "Incorrect.",
            "user_answer": user_answer,
            "correct_answer": question.answer
        })
        
        

        '''
        get the question
        get the choices
        compare the two == OMG
        yahoo its working???
        this is not suyper sigma 
        '''
        