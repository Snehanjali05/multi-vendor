from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class InventoryCategoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryCategory.objects.all()
    serializer_class = InventoryCatgeorySerializer
    
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItem
    
class InventoryStockViewSet(viewsets.ModelViewSet):
    queryset = InventoryStock.objects.all()
    serializer_class = InventoryStockSerializer
    
class InventorySupplierViewSet(viewsets.ModelViewSet):
    queryset = InventorySupplier.objects.all()
    serializer_class = InventorySupplierSerializer
    
class InventoryOrderViewSet(viewsets.ModelViewSet):
    queryset = InventoryOrder.objects.all()
    serializer_class = InventoryOrderSerializer
    
class InventoryOrderItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryOrderItem.objects.all()
    serializer_class = InventoryOrderItemSerializer
    
    
    
router = DefaultRouter()
router.register('inv-category', InventoryCategoryViewSet, 'inv-category')
router.register('inv-item', InventoryItemViewSet, 'inv-item')
router.register('inv-stock', InventoryStockViewSet, 'inv-stock')
router.register('inv-supplier', InventorySupplierViewSet, 'inv-supplier')
router.register('inv-order', InventoryOrderViewSet, 'inv-order')
router.register('inv-order-item', InventoryOrderItemViewSet, 'inv-order-item')


urlpatterns = [
    path('', include(router.urls))
]