from django.db import models
import uuid
from restaurant.models import Restaurant
from enum import Enum
from users.models import User

class status_type(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'CANCELED'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]



class InventoryCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class InventoryItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=16)
    category_id = models.ForeignKey(InventoryCategory, on_delete=models.PROTECT)
    description = models.TextField()
    #unit - kg, liters 
    unit = models.CharField(max_length=8)
    reorder_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class InventoryStock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    quantity = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.item_id.name} - {self.restaurant_id.name}"
    
class InventorySupplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=16, blank=True, null=True)
    contact_name_id = models.IntegerField(User, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class InventoryOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplier_id = models.ForeignKey(InventorySupplier, on_delete=models.PROTECT)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateTimeField()
    status = models.CharField(choices=status_type.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"order {self.id} from {self.supplier_id.name}"
    
    
class InventoryOrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(InventoryOrder, on_delete=models.PROTECT)
    item_id = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)
    quantity = models.FloatField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} of {self.item_id.name}"