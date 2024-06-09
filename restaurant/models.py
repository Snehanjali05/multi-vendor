from django.db import models
from users.models import Address
from enum import Enum
import uuid
from users.models import VendorProfile
from .utils import validate_phone_number, validate_lowercase_email, validate_opening_closing_times
from django.core.validators import MinValueValidator, URLValidator

class DayChoices(Enum):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class CuisineChoices(Enum):
    ITALIAN = 'Italian'
    CHINESE = 'Chinese'
    MEXICAN = 'Mexican'
    INDIAN = 'Indian'
    FRENCH = 'French'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
    
 
class RestaurantCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=8, db_index=True, choices=CuisineChoices.choices())
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
    
class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    vendor_id = models.ForeignKey(VendorProfile, null=False, db_index=True, on_delete=models.PROTECT)
    category_id = models.ForeignKey(RestaurantCategory, db_index=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=128, db_index=True)
    description = models.TextField(blank=True, null=True)
    address_id = models.OneToOneField(Address, on_delete=models.PROTECT)
    mobile = models.CharField(max_length=16, unique=True,db_index=True, validators=[validate_phone_number])
    email = models.EmailField(unique=True, db_index=True, validators=[validate_lowercase_email])
    website = models.URLField(validators=[URLValidator], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
    
class RestaurantPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, null=False, db_index=True, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='restaurant_photos/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo of {self.restaurant_id.name}"
    
    class Meta:
        ordering = ['-uploaded_at']
    
    
class RestaurantRevenue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, null=False, db_index=True, on_delete=models.PROTECT)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, validators=[MinValueValidator(0)])
    avg_cost = models.DecimalField(max_digits=10, decimal_places=2,db_index=True, validators=[MinValueValidator(0)])
    total_orders = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Revenue for {self.restaurant_id.name} on {self.date}"
    
    class Meta:
        ordering = ['-date']
        unique_together = ('restaurant_id', 'date')
    
    
class RestaurantHours(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    restaurant_id = models.ForeignKey(Restaurant, null=False, db_index=True, on_delete=models.PROTECT)
    day_of_week = models.CharField(choices=DayChoices.choices(), max_length=16)
    opening_time = models.TimeField(validators=[validate_opening_closing_times])
    closing_time = models.TimeField(validators=[validate_opening_closing_times])
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.restaurant_id.name} hours on {self.day_of_week}"
    
    class Meta:
        ordering = ['restaurant_id','day_of_week']
        unique_together = ('restaurant_id', 'day_of_week')
    