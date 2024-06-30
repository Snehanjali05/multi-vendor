from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum
import uuid 
from .utils import validate_phone_number, validate_lowercase_email
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator,\
    URLValidator

class GenderType(Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNDEFINED = 'undefined'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class AccountStatusChoice(Enum):
    ACTIVE = 'active'
    DEACTIVATED = 'deactivated'
    SUSPENDED = 'suspended'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
    
class NotificationType(Enum):
    EMAIL = 'email'
    SMS = 'sms'
    PUSH = 'push_notification'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class AvailabilityChoice(Enum):
    AVAILABLE = 'available'
    BUSY = 'busy'
    OFF_DUTY = 'off_duty'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]

class AddressTypeChoice(Enum):
    HOME = 'home'
    WORK = 'work'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]

class PaymentMethodChoice(Enum):
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'
    PAYPAL = 'paypal'
    CASH = 'cash'
    BANK_TRANSFER = 'bank_transfer'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class VehicleTypeChoice(Enum):
    BIKE = 'bike'
    SCOOTER =  'scooter'
    MINI_VAN = 'mini_van'
    ELECTRIC_BIKE = 'electric_bike'
    
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
    address_type = models.CharField(choices=AddressTypeChoice.choices(), max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.address_line1} - {self.city} - {self.country}"
        
        
class User(BaseUser, AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=16, db_index=True)
    mobile = models.CharField(max_length=16, db_index=True, validators=[validate_phone_number])
    email = models.EmailField(unique=True, null=False, db_index=True, validators=[validate_lowercase_email])
    dob = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(choices=GenderType.choices(), max_length=16)
    address_id = models.OneToOneField(Address, on_delete=models.PROTECT)
    preferred_language = models.CharField(max_length=16, default='en')
    preferred_currency = models.CharField(max_length=8, default='USD')
    account_status = models.CharField(choices=AccountStatusChoice.choices(), max_length=16) 
    notification_preferrence = models.CharField(choices=NotificationType.choices(), max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.email}"

    
class VendorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.OneToOneField(User, null=False, db_index=True, on_delete=models.PROTECT)
    business_name = models.CharField(max_length=32)
    business_license = models.CharField(max_length=32, unique=True)
    tax_id = models.CharField(max_length=32, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=False, validators=[validate_lowercase_email])
    mobile = models.CharField(max_length=16, db_index=True, unique=True, null=False, validators=[validate_phone_number])
    business_address = models.OneToOneField(Address, max_length=128, on_delete=models.PROTECT)
    website = models.URLField(validators=[URLValidator])
    social_media_links = models.URLField()
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    total_orders = models.IntegerField()
    account_status = models.CharField(choices=AccountStatusChoice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def updated_rating(self, new_rating):
        self.rating = new_rating
        self.save()
        
    def increment_orders(self):
        self.total_orders += 1
        self.save()
        
    def __str__(self):
        return f"{self.business_name} - {self.email}"

        
    
class CustomerProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.OneToOneField(User, null=False, db_index=True, on_delete=models.PROTECT)
    mobile = models.CharField(max_length=16, null=False, db_index=True, validators=[validate_phone_number])
    email = models.EmailField(db_index=True, unique=True, null=False, validators=[validate_lowercase_email])
    address_id = models.OneToOneField(Address, on_delete=models.PROTECT)
    loyality_points = models.IntegerField(default=0)
    preferred_payment_method = models.CharField(max_length=16, choices=PaymentMethodChoice.choices())
    fav_restaurants = models.ManyToManyField('restaurant.Restaurant')
    fav_dishes = models.ManyToManyField('menu.MenuItem')
    account_status = models.CharField(choices=AccountStatusChoice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def add_loyalty_points(self, points):
        self.loyality_points += points
        self.save()
        
    def redeem_loyalty_points(self, points):
        if self.loyality_points >= points:
            self.loyality_points -= points
            self.save()
            
    def __str__(self):
        return f"{self.user_id.name} - {self.email}"


class DeliveryPersonProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.OneToOneField(User, null=False, db_index=True, on_delete=models.PROTECT)
    mobile = models.CharField(max_length=16,db_index=True,null=False, unique=True, validators=[validate_phone_number])
    email = models.EmailField(db_index=True, unique=True, null=False, validators=[validate_lowercase_email])
    address_id = models.OneToOneField(Address, on_delete=models.PROTECT)
    vehicle_type = models.CharField(max_length=16, choices=VehicleTypeChoice.choices())
    vehicle_number = models.CharField(max_length=16, unique=True, validators=[RegexValidator(
        regex=r'^[A-Z]{2}\d{2}[A-Za-z0-9]{6}$',
        message="enter a valid vehicle number"
    )])
    driver_license = models.CharField(max_length=16, unique=True, validators=[RegexValidator(
        regex=r"^[A-Z]{2}-?\d{2}\d{4}\d+$",
        message="Enter a valid driver license"
    )])
    availability_status = models.CharField(choices=AvailabilityChoice.choices(), max_length=16)
    # current_location 
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    total_deliveries = models.IntegerField()
    account_status = models.CharField(choices=AccountStatusChoice.choices(), max_length=16) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user_id.name} - {self.email}"
