from rest_framework import serializers
from .models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
class NotificationRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationRecipient
        fields = '__all__'
        
class NotificationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStatus
        fields = '__all__'