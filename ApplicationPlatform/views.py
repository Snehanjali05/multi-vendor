from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class PlatformAnalyticViewSet(viewsets.ModelViewSet):
    queryset = PlatformAnalytic.objects.all()
    serializer_class = PlatformAnalyticSerializer
    
class PlatformNotificationViewSet(viewsets.ModelViewSet):
    queryset = PlatformNotification.objects.all()
    serializer_class = PlatformNotificationSerializer
    
class PlatformFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PlatformFeedback.objects.all()
    serializer_class = PlatformFeedbackSerializer
    
class PlatformAdminLogViewSet(viewsets.ModelViewSet):
    queryset = PlatformAdminLog.objects.all()
    serializer_class = PlatformAdminLogSerializer
    
    
router = DefaultRouter()
router.register('platform-analytics', PlatformAnalyticViewSet, 'platform-analytics')
router.register('platform-notification', PlatformNotificationViewSet, 'platform-notification')
router.register('platform-feedback', PlatformFeedbackViewSet, 'platform-feedback')
router.register('platform-admin-log', PlatformAdminLogViewSet, 'platform-admin-log')

urlpatterns = [
    path('', include('router.urls'))
]