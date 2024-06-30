from rest_framework import serializers
from .models import *

class InventoryCatgeorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCategory
        fields = '__all__'
        
class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        
class InventoryStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryStock
        fields = '__all__'
        
class InventorySupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventorySupplier
        fields = '__all__'
        
class InventoryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryOrder
        fields = '__all__'
        
class InventoryOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryOrderItem
        fields = '__all__'
        
