from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    
class VendorProfileViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    
class DeliveryPersonProfileViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPersonProfile.objects.all()
    serializer_class = DeliveryPersonProfileSerializer
    
    
router = DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('address', AddressViewSet, 'address')
router.register('customer', CustomerProfileViewSet, 'customer')
router.register('vendor', VendorProfileViewSet, 'vendor')
router.register('delivery', DeliveryPersonProfileViewSet, 'delivery')


urlpatterns = [
    path('', include(router.urls))
]