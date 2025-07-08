from django.urls import path

from . import views

urlpatterns = [
    path("fdhgiug", views.index, name="index"),
]   