from django.db import models
import uuid
from order.models import Order
from users.models import CustomerProfile, VendorProfile, DeliveryPersonProfile
from restaurant.models import Restaurant
from menu.models import MenuItem
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta


class OrderAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    total_orders = models.IntegerField(validators=[MinValueValidator(0)], db_index=True)
    completed_orders = models.IntegerField(validators=[MinValueValidator(0)], db_index=True)
    pending_orders = models.IntegerField(validators=[MinValueValidator(0)], db_index=True)
    canceled_orders = models.IntegerField(validators=[MinValueValidator(0)], db_index=True)
    avg_order_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Order Analytics {self.id}"
    
    
class CustomerAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    total_customers = models.IntegerField(validators=[MinValueValidator(0)])
    active_customers = models.IntegerField(validators=[MinValueValidator(0)])
    inactive_customers = models.IntegerField(validators=[MinValueValidator(0)])
    avg_spend_per_customer = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    loyal_customers_count = models.IntegerField(validators=[MinValueValidator(0)])
    new_customers = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Customer Analytics {self.id}"
    
    
class VendorAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(VendorProfile, on_delete=models.PROTECT)
    total_vendors = models.IntegerField(validators=[MinValueValidator(0)])
    active_vendors = models.IntegerField(validators=[MinValueValidator(0)])
    inactive_vendors = models.IntegerField(validators=[MinValueValidator(0)])
    total_items_sold = models.IntegerField(validators=[MinValueValidator(0)])
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    total_sales = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Vendor Analytics {self.id}"
      
class DeliveryAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    delivery_person_id = models.ForeignKey(DeliveryPersonProfile, on_delete=models.PROTECT, db_index=True)
    total_deliveries = models.IntegerField(validators=[MinValueValidator(0)])
    successful_deliveries = models.IntegerField(validators=[MinValueValidator(0)])
    failed_deliveries = models.IntegerField(validators=[MinValueValidator(0)])
    avg_delivery_time = models.DurationField(validators=[MinValueValidator(timedelta(seconds=0))])
    delivery_fee_earned = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Delivery Analytics {self.id}"
    
class RestaurantAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    total_visits = models.IntegerField(validators=[MinValueValidator(0)])
    unique_visitors = models.IntegerField(validators=[MinValueValidator(0)])
    total_orders = models.IntegerField(validators=[MinValueValidator(0)])
    total_revenue = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0.01)])
    avg_order_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    review_count = models.IntegerField(validators=[MinValueValidator(0)])
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Restaurant Analytics {self.id}"
    
class PopularItemAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    total_orders = models.IntegerField(validators=[MinValueValidator(0)])
    total_revenue = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Popular Item Analytics {self.id}"
    
            
class ReviewAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    menu_item_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    total_reviews = models.IntegerField(validators=[MinValueValidator(0)])
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    reviews_by_day = models.IntegerField(validators=[MinValueValidator(0)])
    reviews_by_week = models.IntegerField(validators=[MinValueValidator(0)])
    reviews_by_month = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Review Analytics {self.id}"
    
class RevenueAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    total_revenue = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    revenue_by_day = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    revenue_by_week = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    revenue_by_month = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    avg_daily_revenue = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    avg_monthly_revenue = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Revenue Analytics {self.id}"
    
    