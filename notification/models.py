from django.db import models
import uuid
from users.models import CustomerProfile
from enum import Enum

class notification_type(Enum):
    EMAIL = 'email'
    SMS = 'sms'
    PUSH = 'push_notification'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class status_choice(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]



class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    notification_type = models.CharField(choices=notification_type.choices(), max_length=16) #enum
    subject = models.CharField(max_length=64)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
class NotificationRecipient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    preferred_notification_method = models.CharField(choices=notification_type.choices(), max_length=16)
    
class NotificationStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notification_id = models.ForeignKey(Notification, on_delete=models.PROTECT)
    status = models.CharField(choices=status_choice.choices(), max_length=16)
    
    