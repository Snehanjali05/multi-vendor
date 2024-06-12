from django.db import models
import uuid
from restaurant.models import Restaurant
from enum import Enum
from users.models import User, Address
from django.core.validators import MinValueValidator
from .utils import validate_unit, validate_lowercase_email,validate_order_date


class StatusType(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class InventoryCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=32, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    
class InventoryItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=16, unique=True, db_index=True)
    category_id = models.ForeignKey(InventoryCategory, on_delete=models.PROTECT)
    description = models.TextField()
    unit = models.CharField(max_length=8, validators=[validate_unit])
    reorder_level = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class InventoryStock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    item_id = models.ForeignKey(InventoryItem, on_delete=models.PROTECT, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT, db_index=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['item_id', 'restaurant_id']
    
    def __str__(self):
        return f"{self.item_id.name} - {self.restaurant_id.name}"
    
class InventorySupplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=32, db_index=True)
    contact_name_id = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
    email = models.EmailField(validators=[validate_lowercase_email])
    address = models.OneToOneField(Address, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    
class InventoryOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    supplier_id = models.ForeignKey(InventorySupplier, on_delete=models.PROTECT, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT, db_index=True)
    order_date = models.DateTimeField(auto_now_add=True, validators=[validate_order_date])
    expected_delivery_date = models.DateTimeField()
    status = models.CharField(choices=StatusType.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-order_date']
    
    def __str__(self):
        return f"order {self.id} from {self.supplier_id.name}"
    
    
class InventoryOrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(InventoryOrder, on_delete=models.PROTECT, db_index=True)
    item_id = models.ForeignKey(InventoryItem, on_delete=models.PROTECT, db_index=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0.01)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['order_id', 'item_id']
        
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.quantity} of {self.item_id.name}"