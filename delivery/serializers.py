from rest_framework import serializers
from.models import *

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
        
class DeliveryVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryVehicle
        fields = '__all__'
        
class DeliveryFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryFeedback
        fields = '__all__'
        
class DeliveryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryHistory
        fields = '__all__'