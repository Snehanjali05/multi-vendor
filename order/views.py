from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class OrderStatusHistoryViewSet(viewsets.ModelViewSet):
    queryset = OrderStatusHistory.objects.all()
    serializer_class = OrderStatusHistorySerializer
    
router = DefaultRouter()
router.register('order', OrderViewSet, 'order')
router.register('order-item', OrderItemViewSet, 'order-item')
router.register('order-status-history', OrderStatusHistoryViewSet, 'order-status-history')


urlpatterns = [
    path('', include(router.urls))
]