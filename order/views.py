from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import OrderSerializer
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@api_view(['GET'])
def OrderList(request):
    queryset = User.objects.all()
    serializer_class = OrderSerializer(queryset, many=True)
    return Response(serializer_class.data)

@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@api_view(['POST'])
def OrderCreate(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

