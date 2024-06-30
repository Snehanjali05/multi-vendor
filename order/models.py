from django.db import models
import uuid
from users.models import CustomerProfile, Address
from menu.models import MenuItem
from enum import Enum
from django.core.validators import MinValueValidator

class StatusChoice(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class PaymentMethodChoice(Enum):
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'
    PAYPAL = 'paypal'
    CASH = 'cash'
    BANK_TRANSFER = 'bank_transfer'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0.0)])
    status = models.CharField(choices=StatusChoice.choices(), db_index=True, max_length=16) 
    order_time = models.DateTimeField(auto_now_add=True)
    delivery_address = models.ForeignKey(Address, on_delete=models.PROTECT)
    payment_method = models.CharField(choices=PaymentMethodChoice.choices(), max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-order_time']
        
    def __str__(self):
        return f"Order {self.id} by {self.customer_id.user_id.username}"

        
class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_item_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('order_id', 'menu_item_id')
        
    def __str__(self):
        return f"{self.quantity} * {self.menuitem_id.name}"
    
        
    
class OrderStatusHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    status = models.CharField(choices=StatusChoice.choices(), max_length=16) 
    update_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-update_time']
    
    def __str__(self):
        return f"{self.order_id} - {self.status}"
    
    