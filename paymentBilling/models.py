from django.db import models
import uuid
from order.models import Order
from users.models import CustomerProfile
from subscription.models import Subscription
from enum import Enum
from django.core.validators import MinValueValidator
from .utils import validate_due_date, validate_refund_amount


class PaymentMethodChoice(Enum):
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'
    PAYPAL = 'paypal'
    CASH = 'cash'
    BANK_TRANSFER = 'bank_transfer'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class TransactionStatusChoice(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    REFUNDED = 'refunded'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
    
class InvoiceStatusChoice(Enum):
    UNPAID = 'unpaid'
    PAID = 'paid'
    OVERDUE = 'overdue'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class RefundStatusChoice(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class PaymentTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    payment_method = models.CharField(choices=PaymentMethodChoice.choices(), max_length=16)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    transaction_date = models.DateField(auto_now_add=True, db_index=True)
    transaction_id = models.CharField(max_length=32, unique=True, db_index=True)
    status = models.CharField(choices=TransactionStatusChoice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-transaction_date'] 
    
    def __str__(self):
        return f"Transaction {self.transactionId} - {self.amount}"
    
    
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=32, unique=True)
    issued_date = models.DateTimeField(auto_now_add=True, db_index=True)
    due_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    status = models.CharField(choices=InvoiceStatusChoice.choices() , max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-issued_date']
    
    def __str__(self):
        return f"Invoice {self.invoice_number}"
    
    def save(self, *args, **kwargs):
        validate_due_date(self.issued_date, self.due_date)
        super().save(*args, **kwargs)
    
        
class BillingAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    address_line1 = models.CharField(max_length=64)
    address_line2 = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=8)
    country = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.address_line1} - {self.city}"
    
    
class Refund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    payment_transaction_id = models.ForeignKey(PaymentTransaction, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    reason = models.TextField(blank=True, null=True)
    refund_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=RefundStatusChoice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-refund_date']
     
    def __str__(self):
        return f"Refund {self.id} for {self.PaymentTransaction_id.transactionId}"
    
    def save(self, *args, **kwargs):
        validate_refund_amount(self.amount, self.payment_transaction_id.amount)
        super().save(*args, **kwargs)