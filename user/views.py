from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def UserList(request):
    queryset = User.objects.all()
    serializer_class = UserSerializer(queryset, many=True)
    return Response(serializer_class.data)