from django.shortcuts import render

# Create your views here.

def choice(request, question_desc):
    return HttpResponse("You're voting on question " + question_desc)
