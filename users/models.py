from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum
import uuid 
from restaurant.models import Restaurant
from menu.models import MenuItem


class gender_type(Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNDEFINED = 'undefined'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class acc_status_choice(Enum):
    ACTIVE = 'active'
    DEACTIVATED = 'deactivated'
    SUSPENDED = 'suspended'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
    
class notification_type(Enum):
    EMAIL = 'email'
    SMS = 'sms'
    PUSH = 'push_notification'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class availability_choice(Enum):
    AVAILABLE = 'available'
    BUSY = 'busy'
    OFF_DUTY = 'off_duty'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]




class BaseUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at']
        
        
class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address_line1 = models.CharField(max_length=128)
    address_line2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=8)
    country = models.CharField(max_length=32)
    address_type = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
        
class User(BaseUser, AbstractUser):
    name = models.CharField(max_length=16, db_index=True)
    mobile = models.CharField(max_length=16)
    email = models.EmailField(unique=True, null=False, db_index=True)
    dob = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(choices=gender_type.choices(), max_length=16)
    address_id = models.ForeignKey(Address, on_delete=models.PROTECT)
    preferred_language = models.CharField(max_length=16, default='en')
    preferred_currency = models.CharField(max_length=8, default='USD')
    account_status = models.CharField(choices=acc_status_choice.choices(), max_length=16) 
    notification_preferrence = models.CharField(choices=notification_type.choices(), max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class VendorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, null=False, db_index=True, on_delete=models.PROTECT)
    bussiness_name = models.CharField(max_length=32)
    bussiness_license = models.CharField(max_length=32)
    tax_id = models.CharField(max_length=32)
    mobile = models.CharField(max_length=16)
    bussiness_address = models.CharField(max_length=128)
    website = models.URLField()
    socialmedia_links = models.URLField()
    description = models.TextField()
    rating = models.FloatField()
    total_orders = models.IntegerField()
    account_status = models.CharField(choices=acc_status_choice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class CustomerProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, null=False, db_index=True, on_delete=models.PROTECT)
    mobile = models.CharField(max_length=16)
    address_id = models.ForeignKey(Address, on_delete=models.PROTECT)
    loyality_points = models.IntegerField()
    preferred_payment_method = models.CharField(max_length=16)
    order_history = models.TextField()
    fav_restaurants = models.ManyToManyField(Restaurant)
    fav_dishes = models.ManyToManyField(MenuItem)
    account_status = models.CharField(choices=acc_status_choice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class DeliveryPersonProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, null=False, db_index=True, on_delete=models.PROTECT)
    mobile = models.CharField(max_length=16)
    vehicle_type = models.CharField(max_length=8)
    vehicle_number = models.CharField(max_length=16)
    driver_license = models.CharField(max_length=16)
    availability_status = models.CharField(choices=availability_choice.choices(), max_length=16)
    # current_location 
    rating = models.FloatField()
    total_deliveries = models.IntegerField()
    account_status = models.CharField(choices=acc_status_choice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    