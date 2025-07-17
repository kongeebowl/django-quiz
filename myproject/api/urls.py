from django.urls import path
<<<<<<< HEAD
from .views import QuestionView, UsersView, QuestionViewById, ChoicesView, QuizView, QuizViewById
=======
from .views import QuestionView, UsersView, AwesomeQuestionView, ChoicesView, QuizView, AwesomeQuizView
>>>>>>> parent of aac3a95 (s)


urlpatterns = [
    path('questions/', QuestionView.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionViewById.as_view(), name='question'),

    path('users/', UsersView.as_view(), name='users'),
    path('choices/', ChoicesView.as_view(), name='choices'),

    path('quizzes/', QuizView.as_view(), name='quiz_list'),
<<<<<<< HEAD
    path('quizzes/<int:pk>/', QuizViewById.as_view(), name='quiz_detail'),
=======
    path('quizzes/<int:pk>/', AwesomeQuizView.as_view(), name='quiz_detail'),
>>>>>>> parent of aac3a95 (s)
]