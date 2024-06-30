from rest_framework import serializers
from .models import *

class OrderAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAnalytics
        fields = '__all__'
        
class ReviewAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAnalytics
        fields = '__all__' 

class VendorAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAnalytics
        fields = '__all__'
        
class RevenueAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueAnalytics
        fields = '__all__'
        
class CustomerAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAnalytics
        fields = '__all__'
        
class DeliveryAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAnalytics
        fields = '__all__'
        
class RestaurantAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAnalytics
        fields = '__all__'
        
class PopularItemAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularItemAnalytics
        fields = '__all__'