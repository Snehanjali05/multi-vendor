from django.db import models
import uuid
from order.models import Order
from users.models import DeliveryPersonProfile, CustomerProfile, Address
from enum import Enum
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from .utils import validate_capacity, validate_delivery_times

class VehicleTypeChoice(Enum):
    BIKE = 'bike'
    SCOOTER =  'scooter'
    MINI_VAN = 'mini_van'
    ELECTRIC_BIKE = 'electric_bike'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class StatusChoice(Enum):
    PENDING = 'pending'
    IN_TRANSIT = 'in_transit'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    

class DeliveryVehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    registration_number = models.CharField(max_length=32, db_index=True, validators=[RegexValidator(
        regex=r'^[A-Z]{2}\d{2}[A-Za-z0-9]{6}$',
        message="enter a valid registration number"
    )])
    model = models.CharField(max_length=32, validators=[RegexValidator(
        regex="^[A-Za-z0-9 ]+$",
        message = "Model name must be alphanumeric and can contain spaces"
    )])
    vehicle_type = models.CharField(choices=VehicleTypeChoice.choices(), db_index=True, max_length=16)
    capacity = models.CharField(max_length=64, validators=[validate_capacity])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.registration_number
    
class Delivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    delivery_person_id = models.ForeignKey(DeliveryPersonProfile, on_delete=models.PROTECT)
    assigned_vehicle_id = models.ForeignKey(DeliveryVehicle, on_delete=models.PROTECT)
    status = models.CharField(choices=StatusChoice.choices(), max_length=16) 
    delivery_address = models.ForeignKey(Address, on_delete=models.PROTECT)
    expected_delivery_time = models.DateTimeField()
    actual_delivery_time = models.DateField(null=True, blank=True, validators=[validate_delivery_times])
    tip = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Delivery for order {self.order_id.id}"
    
class DeliveryFeedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField()
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return f"Feedback for Delivery {self.delivery_id.id}"
    
class DeliveryHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    status = models.CharField(choices=StatusChoice.choices(), max_length=16)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.delivery_id} - {self.status}"
