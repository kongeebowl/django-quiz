from django.urls import path
from .views import ItemsView,UsersView


urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
    path('users/', UsersView.as_view(), name='users')
]