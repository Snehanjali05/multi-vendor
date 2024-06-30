from rest_framework import serializers
from .models import *

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

    def validate_discount_percentage(self, value):
        if not (0 <= value <= 100):
            raise serializers.ValidationError('Discount percentage must be between 0 and 100.')
        return value

    def validate_end_date(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError('End date must be after the start date.')
        return data

class PromotionUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionUsage
        fields = '__all__'

    def validate(self, data):
        if PromotionUsage.objects.filter(
            promotion_id=data['promotion_id'], 
            customer_id=data['customer_id'], 
            order_id=data['order_id']
        ).exists():
            raise serializers.ValidationError('You have already used this promotion for this order.')
        return data

class PromotionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionTag 
        fields = '__all__'
