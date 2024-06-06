from django.db import models
from users.models import User
from enum import Enum
import uuid
from users.models import VendorProfile


class RestaurantCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #name- italian, chinese
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(VendorProfile, null=False, db_index=True, on_delete=models.PROTECT)
    category_id = models.ForeignKey(RestaurantCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=256)
    description = models.TextField()
    address = models.CharField(max_length=128)
    mobile = models.CharField(max_length=16)
    email = models.EmailField()
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class RestaurantPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.ForeignKey(Restaurant, null=False, db_index=True, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='restaurant_photos/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo of {self.restaurant_id.name}"
    
    
class RestaurantRevenue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.ForeignKey(Restaurant, null=False, db_index=True, on_delete=models.PROTECT)
    total_revenue = models.DecimalField(max_digits=5, decimal_places=2)
    avg_cost = models.DecimalField()
    total_orders = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Revenue for {self.restaurant_id.name} on {self.date}"
    
class RestaurantHours(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.ForeignKey(Restaurant, null=False, db_index=True, on_delete=models.PROTECT)
    day_of_week = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.restaurant_id.name} hours on {self.day_of_week}"