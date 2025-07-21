from django.urls import path
from .views import QuestionView, UsersView, QuestionViewById, QuizView, QuizViewById, CheckQuiz


urlpatterns = [
    path('questions/', QuestionView.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionViewById.as_view(), name='question'),

    path('users/', UsersView.as_view(), name='users'),


    path('quizzes/', QuizView.as_view(), name='quiz_list'),
    path('quizzes/<int:pk>/', QuizViewById.as_view(), name='quiz_detail'),

    path('check/<int:pk>/', CheckQuiz.as_view(), name='check')
]