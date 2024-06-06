from django.db import models
import uuid
from order.models import Order
from users.models import DeliveryPersonProfile, CustomerProfile

class DeliveryVehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration_number = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    vehicle_type = models.CharField(max_length=16)
    capacity = models.CharField(max_length=64)
    
    def __str__(self):
        return self.registration_number
    
class Delivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    delivery_person_id = models.ForeignKey(DeliveryPersonProfile, on_delete=models.PROTECT)
    assigned_vehicle_id = models.ForeignKey(DeliveryVehicle, on_delete=models.PROTECT)
    status = models.CharField(max_length=16) 
    delivery_address = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    expected_delivery_time = models.DateTimeField()
    actual_delivery_time = models.DateField()
    tip = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"Delivery for order {self.order_id.id}"
    
class DeliveryFeedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    rating = models.IntegerField()
    feedback = models.TextField()
    
    def __str__(self):
        return f"Feedback for Delivery {self.delivery_id.id}"
    
class DeliveryHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    status = models.CharField(max_length=16)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.delivery_id} - {self.status}"
