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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    recipient_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    notification_type = models.CharField(choices=notification_type.choices(), max_length=32)
    subject = models.CharField(max_length=64, null=False)
    message = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-sent_at']
        
    def __str__(self):
        return f"{self.subject} - {self.recipient_id}"
        
    
class NotificationRecipient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT)
    preferred_notification_method = models.CharField(choices=notification_type.choices(), max_length=32)
    
    def __str__(self):
        return f"{self.user_id} - {self.preferred_notification_method}"
        
class NotificationStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    notification_id = models.ForeignKey(Notification, on_delete=models.PROTECT)
    status = models.CharField(choices=status_choice.choices(), max_length=16)
    
    def __str__(self):
        return f"{self.notification_id} - {self.status}"
    