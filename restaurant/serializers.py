from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        
class RestaurantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCategory
        fields = '__all__'
        
class RestaurantPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantPhoto
        fields = '__all__'
        
class RestaurantRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantRevenue
        fields = '__all__'
        
class RestaurantHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantHours
        fields = '__all__'
        