from rest_framework import serializers
from .models import *

class PlatformAnalyticSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformAnalytic
        fields = '__all__'
        
class PlatformNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformNotification
        fields = '__all__'
        
class PlatformFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformFeedback
        fields = '__all__'

class PlatformAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformAdminLog
        fields = '__all__'