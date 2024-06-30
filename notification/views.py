from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
class NotificationRecipientViewSet(viewsets.ModelViewSet):
    queryset = NotificationRecipient.objects.all()
    serializer_class = NotificationRecipientSerializer

class NotificationStatusViewSet(viewsets.ModelViewSet):
    queryset = NotificationStatus.objects.all()
    serializer_class = NotificationStatusSerializer
    

router = DefaultRouter()
router.register('notify', NotificationViewSet, 'notify')
router.register('notify-recipient', NotificationRecipientViewSet, 'notify-recipient')
router.register('notify-status', NotificationStatusViewSet, 'notify-status')

    
urlpatterns = [
    path('', include(router.urls))
]
