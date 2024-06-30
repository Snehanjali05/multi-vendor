from django.db import models
import uuid
from users.models import CustomerProfile, User
from enum import Enum
from django.core.validators import MinValueValidator, MaxValueValidator

class NotificationType(Enum):
    EMAIL = 'email'
    SMS = 'sms'
    PUSH = 'push_notification'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class StatusType(Enum):
    SENT = 'sent'
    PENDING = 'pending'
    FAILED = 'failed'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class PlatformAnalytic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_visits = models.IntegerField(db_index=True, validators=[MinValueValidator(0)])
    unique_visitors = models.IntegerField(validators=[MinValueValidator(0)])
    page_views = models.IntegerField(validators=[MinValueValidator(0)])
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, validators=[MinValueValidator(0)])
    avg_session_duration = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    bounce_rate = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Analytics as of {self.created_at}"
    
class  PlatformNotification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    content = models.TextField()
    recipients = models.ManyToManyField(CustomerProfile)
    notification_type = models.CharField(choices=NotificationType.choices(), max_length=32, db_index=True)
    status = models.CharField(choices=StatusType.choices(), max_length=8, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Notification: {self.title}"
    
class PlatformFeedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT, db_index=True)
    feedback = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Feedback by {self.user_id} with rating {self.rating}"
    
class PlatformAdminLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_user = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.CharField(max_length=128)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Admin log by {self.admin_user} : {self.action}"