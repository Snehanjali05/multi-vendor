from django.db import models
import uuid
from restaurant.models import Restaurant
from users.models import CustomerProfile
from menu.models import MenuItem
from enum import Enum


class reaction_choice(Enum):
    LIKE = 'like'
    DISLIKE = 'dislike'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]



class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    dish_id = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Review by {self.customer_id.username} for {self.restaurant_id or self.dish_id}"
        
    
class ReviewComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review_id = models.ForeignKey(Review, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.customer_id.username} on {self.review_id}"
    
    
class ReviewReaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review_id = models.ForeignKey(Review, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    reaction = models.CharField(choices=reaction_choice.choices(), max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.reaction} by {self.customer_id.username} on {self.review_id}"