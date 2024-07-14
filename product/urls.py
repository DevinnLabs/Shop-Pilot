from django.urls import path

from .views import ProductCreate, ProductList, ProductDetail, ProductUpdate, ProductDelete

urlpatterns = [
    path('create/', ProductCreate, name='product-create'),
    path('list/', ProductList, name='product-list'),
    path('detail/<str:pk>/', ProductDetail, name='product-detail'),
    path('update/<str:pk>/', ProductUpdate, name='product-update'),
    path('delete/<str:pk>/', ProductDelete, name='product-delete'),
]