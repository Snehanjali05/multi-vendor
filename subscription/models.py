from django.db import models
import uuid
from users.models import CustomerProfile
from enum import Enum

class plan_type(Enum):
    BASIC = 'basic'
    PREMIUM = 'premium'
    ENTERPRISE = 'enterprise'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class status_type(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CANCELED = 'canceled'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]



class SubscriptionPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    plan_type = models.CharField(choices=plan_type.choices(), max_length=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration_days = models.IntegerField()
    features = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    plan_id = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    auto_renew = models.BooleanField(default=True)
    status = models.CharField(choices=status_type.choices(), max_length=8) #enum
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class SubscriptionHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    plan_id = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=status_type.choices(), max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    
    