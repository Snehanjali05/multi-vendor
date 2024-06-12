from django.db import models
import uuid
from users.models import CustomerProfile
from enum import Enum
from django.core.validators import MinValueValidator
from .utils import validate_end_date


class PlanType(Enum):
    BASIC = 'basic'
    PREMIUM = 'premium'
    ENTERPRISE = 'enterprise'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class StatusType(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CANCELED = 'canceled'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]



class SubscriptionPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=32)
    plan_type = models.CharField(choices=PlanType.choices(), max_length=16, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    duration_days = models.IntegerField(validators=[MinValueValidator(1)])
    features = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    plan_id = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    auto_renew = models.BooleanField(default=True)
    status = models.CharField(choices=StatusType.choices(), max_length=8) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['start_date']
        
    def  __str__(self):
        return f"{self.user_id} - {self.plan_id}"
    
    def save(self, *args, **kwargs):
        validate_end_date(self.start_date, self.end_date)
        super().save(*args, **kwargs)
    
    
class SubscriptionHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    plan_id = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    status = models.CharField(choices=StatusType.choices(), max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-start_date']
        
    def __str__(self):
        return f"{self.user_id} - {self.plan_id}"
    
    def save(self, *args, **kwargs):
        validate_end_date(self.start_date, self.end_date)
        super().save(*args, **kwargs)