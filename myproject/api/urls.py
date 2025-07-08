from django.urls import path
from .views import QuestionView, UsersView


urlpatterns = [
    path('questions/', QuestionView.as_view(), name='questions'),
    path('users/', UsersView.as_view(), name='users')
]