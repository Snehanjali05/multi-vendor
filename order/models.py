from django.db import models
import uuid
from users.models import CustomerProfile
from menu.models import MenuItem
from enum import Enum

class status_choice(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(choices=status_choice.choices(), max_length=16) 
    order_time = models.DateTimeField(auto_now_add=True)
    delivery_address = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)  # address
    payment_method = models.CharField(max_length=16)
    
    def __str__(self):
        return f"Order {self.id} by {self.customer_id.user_id.username}"
    
class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    menuitem_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} * {self.menuitem_id.name}"
    
class OrderStatusHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    status = models.CharField(choices=status_choice.choices(), max_length=16) 
    update_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.order_id}-{self.status}"
    
