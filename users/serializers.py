from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['created_at', 'updated_at', 'is_active']
        fields_read_only = ['created_at', 'updated_at']
        
        
class UserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def validate(self, attrs):
        password = attrs.get('password', None)
        if password is not None:
            attrs['password'] = make_password(password)
        return super().validate(attrs)
        

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'
        
class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = '__all__'
        
class DeliveryPersonProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPersonProfile
        fields = '__all__'
        
        
