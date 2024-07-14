from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@api_view(['GET'])
def ProductList(request):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer(queryset, many=True)
    return Response(serializer_class.data)

@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@api_view(['POST'])
def ProductCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@api_view(['GET'])
def ProductDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@api_view(['POST'])
def ProductUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@api_view(['DELETE'])
def ProductDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product deleted successfully')
