from rest_framework import serializers
from .models import *

class LoyaltyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = '__all__'
        
class LoyaltyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyMember
        fields = '__all__'
        
class LoyaltyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyTransaction
        fields = '__all__'
        
class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
        
class RedemptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redemption
        fields = '__all__'