from django.urls import path
from .views import ItemsView,UsersView


urlpatterns = [
    path('questions/', QuestionView.as_view(), name='questions'),
    path('users/', UsersView.as_view(), name='users')
]