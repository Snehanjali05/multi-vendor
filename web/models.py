from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
        
class User(BaseUser, AbstractUser):
    name = models.CharField(max_length=16, db_index=True)
    mobile = models.CharField(max_length=16)
    email = models.EmailField(unique=True, null=False, db_index=True)
    dob = models.DateTimeField()
    door_no = models.CharField(max_length=16, null=True)
    street = models.CharField(max_length=16, null=True)
    landmark = models.CharField(max_length=16, null=True)
    sub_area = models.CharField(max_length=16, null=True)
    address1 = models.CharField(max_length=512, null=True)
    city = models.CharField(max_length=16)
    pincode = models.CharField(max_length=8, null=True)
    gender = models.CharField( max_length=16)