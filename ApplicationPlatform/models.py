from django.db import models
import uuid
from users.models import CustomerProfile, User
from enum import Enum

class notification_type(Enum):
    EMAIL = 'email'
    SMS = 'sms'
    PUSH = 'push_notification'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class status_type(Enum):
    SENT = 'sent'
    PENDING = 'pending'
    FAILED = 'failed'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]


class PlatformAnalytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_visits = models.IntegerField()
    unique_visitors = models.IntegerField()
    page_views = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=5, decimal_places=2)
    avg_session_duration = models.DecimalField(max_digits=5, decimal_places=2)
    bounce_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class  PlatformNotifications(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    content = models.TextField()
    recipients = models.ManyToManyField(CustomerProfile)
    notification_type = models.CharField(choices=notification_type.choices(), max_length=32)
    status = models.CharField(choices=status_type.choices(), max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class PlatformFeedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    feedback = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class PlatformAdminLogs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_user = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.CharField(max_length=128)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    