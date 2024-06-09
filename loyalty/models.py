from django.db import models
import uuid
from users.models import CustomerProfile
from order.models import Order
from enum import Enum

class status_type(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    BANNED = 'banned'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
    
class activity_type_choice(Enum):
    EARN = 'earn'
    REDEEM = 'redeem'
    ADJUSTMENT = 'adjustment'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class redemption_status(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    

class LoyaltyProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    description = models.TextField()
    points_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    max_points_per_transaction = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class LoyaltyMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT) 
    loyalty_program_id = models.ForeignKey(LoyaltyProgram, on_delete=models.PROTECT) 
    join_date = models.DateTimeField(auto_now_add=True) 
    points_balance = models.IntegerField(default=0) 
    status = models.CharField(choices=status_type.choices(), max_length=8) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user_id} - {self.loyalty_program_id}"


class LoyaltyTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_id = models.ForeignKey(LoyaltyMember, on_delete=models.PROTECT)
    activity_type = models.CharField(choices=activity_type_choice.choices(), max_length=16)
    points = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True) 
    description = models.TextField(null=True, blank=True) 

    def __str__(self):
        return f"{self.member_id} - {self.activity_type} - {self.points} ponits"

class Reward(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64) 
    description = models.TextField() 
    points_required = models.IntegerField()  
    available_quantity = models.IntegerField() 
    start_date = models.DateTimeField() 
    end_date = models.DateTimeField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.name

class Redemption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_id = models.ForeignKey(LoyaltyMember, on_delete=models.PROTECT) 
    reward_id = models.ForeignKey(Reward, on_delete=models.PROTECT) 
    redemption_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField() 
    status = models.CharField(choices=redemption_status.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return f"{self.member_id} - {self.reward_id} - {self.status}"

