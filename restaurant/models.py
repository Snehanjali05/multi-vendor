from django.db import models
from users.models import User
from enum import Enum


class payment_type(Enum):
    CASH = 'cash'
    CARD = 'card'
    UPI = 'upi'
    PAYPAL = 'paypal'
    RAZORPAY = 'razorpay'
    
    @classmethod
    def choices(cls):
        enum_choices=[]
        for enum in cls:
            enum_choices.append((enum.value, enum.name))
        return enum_choices
    
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    rating = models.DecimalField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    city =  models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    address = models.CharField(max_length=216)
    google_place_id = models.CharField(max_length=16)
    owner = models.CharField(max_length=16)
    menu_id = models.IntegerField()
    user_id = models.IntegerField()
    items = models.ManyToManyField(Item)
    email = models.CharField()
    mobile = models.CharField(max_length=16)
    no_of_reviews = models.IntegerField()
    

class order(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User)
    Restaurant = models.ForeignKey(Restaurant)
    item = models.ForeignKey(Item)
    mode_of_payment =  models.CharField(choices=payment_type.choices, max_length=8)
    