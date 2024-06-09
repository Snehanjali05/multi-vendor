from django.db import models
import uuid
from restaurant.models import Restaurant
from enum import Enum
from django.core.validators import MinValueValidator

class TagChoices(Enum):
    CHEFS_SPECIAL = 'Chefs_Special'
    NEW = 'New'
    POPULAR = 'Popular'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    name =  models.CharField(max_length=64, db_index=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']
        
    
class MenuCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT)
    name = models.CharField(max_length=64, db_index=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']
    
    
class MenuItemImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='menuitems/')
    
    def __str__(self):
        return self.image
    
       
class MenuItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=128, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0)])
    images = models.ManyToManyField(MenuItemImage,related_name='menu_items', blank=True)
    is_veg = models.BooleanField(default=True, db_index=True)
    is_spicy = models.BooleanField(default=True, db_index=True)
    is_available = models.BooleanField(default=True)
    # preparation_time = models.DurationField()
    tag = models.CharField(choices=TagChoices.choices(), max_length=16, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
