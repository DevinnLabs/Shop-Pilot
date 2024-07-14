from django.urls import path

from .views import OrderCreate, OrderList

urlpatterns = [
    path('create/', OrderCreate, name='order-create'),
    path('list/', OrderList, name='order-list'),
]