from django.db import models
import uuid
from restaurant.models import Restaurant


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    name =  models.CharField(max_length=64)
    description = models.TextField(blan=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
class MenuCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
class MenuItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menuitems/')
    is_veg = models.BooleanField(default=True)
    is_spicy = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    preparation_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    