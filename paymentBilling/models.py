from django.db import models
import uuid
from order.models import Order
from users.models import CustomerProfile
from subscription.models import Subscription
from enum import Enum

class payment_method_choice(Enum):
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'
    PAYPAL = 'paypal'
    CASH = 'cash'
    BANK_TRANSFER = 'bank_transfer'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class transaction_status_choice(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    REFUNDED = 'refunded'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
    
class invoice_status_choice(Enum):
    UNPAID = 'unpaid'
    PAID = 'paid'
    OVERDUE = 'overdue'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class refund_status_choice(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class PaymentTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    payment_method = models.CharField(choices=payment_method_choice.choices(), max_length=16)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    transaction_date = models.DateField(auto_now_add=True)
    transactionId = models.CharField(max_length=16)
    status = models.CharField(choices=transaction_status_choice.choices(), max_length=16, unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.transactionId} - {self.amount}"
    
    
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=16, unique=True)
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(choices=invoice_status_choice.choices() , max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.invoice_number
    
        
class BillingAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    address_line1 = models.CharField(max_length=64)
    address_line2 = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=8)
    country = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.address_line1} - {self.city}"
    
    
class Refund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PaymentTransaction_id = models.ForeignKey(PaymentTransaction, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    reason = models.TextField(blank=True, null=True)
    refund_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=refund_status_choice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return f"Refund {self.id} for {self.PaymentTransaction_id.transactionId}"
    