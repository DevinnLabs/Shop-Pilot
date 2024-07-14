from django.urls import path

from .views import UserCreate, UserList

urlpatterns = [
    path('create/', UserCreate, name='user-create'),
    path('list/', UserList, name='user-list'),
]