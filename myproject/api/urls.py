from django.urls import path
from .views import QuestionView, UsersView, AwesomeQuestionView,ChoicesView


urlpatterns = [
    path('questions/', QuestionView.as_view(), name='question_list'),
    path('questions/<int:pk>/', AwesomeQuestionView.as_view(), name='question'),
    path('users/', UsersView.as_view(), name='users'),
    path('choices/', ChoicesView.as_view(), name='choices')

]