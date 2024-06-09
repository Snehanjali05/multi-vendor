from django.db import models
import uuid
from restaurant.models import Restaurant
from users.models import CustomerProfile
from order.models import Order
from enum import Enum

class tag_choice(Enum):
    HOLIDAY_SPL = 'holiday_spl'
    SUMMER_SALE = 'summer_sale'
    WINTER_DISCOUNT = 'winter_discount'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]

class promotion_type_choice(Enum):
    DISCOUNT = 'discount'
    BOGO = 'buy_one_get_one_free'
    CASHBACK = 'cashback'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class Promotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    promotion_type = models.CharField(choices=promotion_type_choice.choices(), max_length=32, db_index=True) 
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    promo_code = models.CharField(max_length=32, unique=True, db_index=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = [('promo_code', 'restaurant_id')]
        
    def __str__(self):
        return f"{self.promotion_type} - {self.restaurant_id.name}"
     
class PromotionUsage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    promotion_id = models.ForeignKey(Promotion, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    usage_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-usage_date']
    
    def __str__(self):
        return f"{self.promotion_id.promotion_type} used by {self.customer_id.user_id.username} on order {self.order_id.id}"
    
class PromotionTag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    promotion_id = models.ForeignKey(Promotion, on_delete=models.PROTECT)
    tag = models.CharField(choices=tag_choice.choices(), max_length=16, db_index=True)
    
    class Meta:
        ordering = ['tag']
        
    def __str__(self):
        return f"{self.tag} for {self.promotion_id.promotion_type}"