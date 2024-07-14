from django.shortcuts import render

from user.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

@csrf_exempt
@api_view(['POST'])
def signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'}, status='400')
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Username already exists'}, status='400')
    user = User.objects.create_user(username=email, password=password)
    refresh = RefreshToken.for_user(user)
    return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})

@csrf_exempt
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials'}, status='400')
    refresh = RefreshToken.for_user(user)
    return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})

@csrf_exempt
@api_view(['POST'])
def refresh(request):
    refresh_token = request.data.get('refresh')
    try:
        token = RefreshToken(refresh_token)
        access_token = str(token.access_token)
        return Response({'access': access_token})
    except Exception as e:
        return Response({'error': 'Invalid refresh token'}, status='400')
    
@csrf_exempt
@api_view(['GET'])
def get_user_from_token(request):
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            authentication = JWTAuthentication()
            user, _ = authentication.authenticate_credentials(token)
            return Response({'email': user.email})
        else:
            return Response({'error': 'Invalid token'}, status='400')
    except Exception as e:
        return Response({'error': 'Invalid token'}, status='400')