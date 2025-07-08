from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from Quiz.polls.serializers import GroupSerializer, UserSerializer

def index(request):
    latest_question_list = Question.objects.order_by("-date_posted")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def selected(request,question_id):
    return HttpResponse("Hey this is the question u are selecting " +  str(question_id))

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]