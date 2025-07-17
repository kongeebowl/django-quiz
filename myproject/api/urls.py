from django.urls import path
from .views import *

urlpatterns = [
    path('questions/', QuestionView.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionViewById.as_view(), name='question'),

    path('users/', UsersView.as_view(), name='users'),
    path('choices/', ChoicesView.as_view(), name='choices'),
    path('api/login/', LoginView.as_view()),
    path('quizzes/', QuizView.as_view(), name='quiz_list'),
    path('quizzes/<int:pk>/', QuizViewById.as_view(), name='quiz_detail'),
]