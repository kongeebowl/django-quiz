from django.urls import path
from .views import QuestionView, UsersView, AwesomeQuestionView


urlpatterns = [
    path('questions/', QuestionView.as_view(), name='question_list'),
    path('questions/<int:pk>/', AwesomeQuestionView.as_view(), name='question'),
    path('users/', UsersView.as_view(), name='users')
]