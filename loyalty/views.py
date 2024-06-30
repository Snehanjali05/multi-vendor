from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class LoyaltyProgramViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer
    
class LoyaltyMemberViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyMember.objects.all()
    serializer_class = LoyaltyMemberSerializer
    
class LoyaltyTransactionViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyTransaction.objects.all()
    serializer_class = LoyaltyTransactionSerializer
    
class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    
class RedemptionViewSet(viewsets.ModelViewSet):
    queryset = Redemption.objects.all()
    serializer_class = RedemptionSerializer
    
    
router = DefaultRouter()
router.register('loyalty-program', LoyaltyProgramViewSet, 'loyalty-program')
router.register('loyalty-member', LoyaltyMemberViewSet, 'loyalty-member')
router.register('loyalty-transaction', LoyaltyTransactionViewSet, 'loyalty-transaction')
router.register('reward', RewardViewSet, 'reward')
router.register('redemption', RedemptionViewSet, 'redemption')

urlpatterns = [
    path('', include(router.urls))
]