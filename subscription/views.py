from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubsriptionSerializer
    
class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubsriptionPlanSerializer

class SubscriptionHistoryViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionHistory.objects.all()
    serializer_class = SubsriptionHistorySerializer
    
    
router = DefaultRouter()
router.register('subscript', SubscriptionViewSet, 'subscript')
router.register('subscript-plan', SubscriptionPlanViewSet, 'subscript-plan')
router.register('subscript-history', SubscriptionHistoryViewSet, 'subscript-history')

urlpatterns = [
    path('', include(router.urls))
]
