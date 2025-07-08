from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're  the polls index.")

def selected():
    return HttpResponse("Hey this is the question u are selecting")