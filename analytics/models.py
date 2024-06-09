from django.db import models
import uuid
from order.models import Order
from users.models import CustomerProfile, VendorProfile, DeliveryPersonProfile
from restaurant.models import Restaurant
from menu.models import MenuItem


class OrderAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT, db_index=True)
    total_orders = models.IntegerField()
    completed_orders = models.IntegerField()
    pending_orders = models.IntegerField()
    canceled_orders = models.IntegerField()
    avg_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Order Analytics {self.id}"
    
    
class CustomerAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT, db_index=True)
    total_customers = models.IntegerField()
    active_customers = models.IntegerField()
    inactive_customers = models.IntegerField()
    avg_spend_per_customer = models.DecimalField(max_digits=10, decimal_places=2)
    loyal_customers_count = models.IntegerField()
    new_customers = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Customer Analytics {self.id}"
    
    
class VendorAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    vendor_id = models.ForeignKey(VendorProfile, on_delete=models.PROTECT, db_index=True)
    total_vendors = models.IntegerField()
    active_vendors = models.IntegerField()
    inactive_vendors = models.IntegerField()
    total_items_sold = models.IntegerField()
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    total_sales = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Vendor Analytics {self.id}"
      
class DeliveryAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    delivery_person_id = models.ForeignKey(DeliveryPersonProfile, on_delete=models.PROTECT, db_index=True)
    total_deliveries = models.IntegerField()
    successful_deliveries = models.IntegerField()
    failed_deliveries = models.IntegerField()
    avg_delivery_time = models.DurationField()
    delivery_fee_earned = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Delivery Analytics {self.id}"
    
class RestaurantAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT, db_index=True)
    total_visits = models.IntegerField()
    unique_visitors = models.IntegerField()
    total_orders = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    avg_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    review_count = models.IntegerField()
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Restaurant Analytics {self.id}"
    
class PopularItemAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    item_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT, db_index=True)
    total_orders = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Popular Item Analytics {self.id}"
    
            
class ReviewAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    menu_item_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    total_reviews = models.IntegerField()
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    reviews_by_day = models.IntegerField()
    reviews_by_month = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Review Analytics {self.id}"
    
class RevenueAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    total_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    revenue_by_day = models.DecimalField(max_digits=20, decimal_places=2)
    revenue_by_week = models.DecimalField(max_digits=20, decimal_places=2)
    revenue_by_month = models.DecimalField(max_digits=20, decimal_places=2)
    avg_daily_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    avg_monthly_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Revenue Analytics {self.id}"
    
    