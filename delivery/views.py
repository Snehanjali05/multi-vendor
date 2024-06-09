from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    
class DeliveryVehicleViewSet(viewsets.ModelViewSet):
    queryset = DeliveryVehicle.objects.all()
    serializer_class = DeliveryVehicleSerializer
    
class DeliveryFeedbackViewSet(viewsets.ModelViewSet):
    queryset = DeliveryFeedback.objects.all()
    serializer_class = DeliveryFeedbackSerializer

class DeliveryHistoryViewSet(viewsets.ModelViewSet):
    queryset = DeliveryHistory.objects.all()
    serializer_class = DeliveryHistorySerializer
    
    
router = DefaultRouter()
router.register('del', DeliveryViewSet, 'del')
router.register('del-vehicle', DeliveryVehicleViewSet, 'del-vehicle')
router.register('del-feedback', DeliveryFeedbackViewSet, 'del-feedback')
router.register('del-history', DeliveryHistoryViewSet, 'del-history')

urlpatterns = [
    path('', include(router.urls))
]