from django.urls import path
from .views import signup, login, refresh

urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', login, name='login'),
    path('refresh/', refresh, name='refresh'),
]