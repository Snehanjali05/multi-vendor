from rest_framework import viewsets
from .serilaizers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class OrderAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = OrderAnalytics.objects.all()
    serializer_class = OrderAnalyticsSerializer

class ReviewAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = ReviewAnalytics.objects.all()
    serializer_class = ReviewAnalyticsSerializer
    
class VendorAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = VendorAnalytics.objects.all()
    serializer_class = VendorAnalyticsSerializer
    
class RevenueAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = RevenueAnalytics.objects.all()
    serializer_class = RevenueAnalyticsSerializer
    
class CustomerAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = CustomerAnalytics.objects.all()
    serializer_class = CustomerAnalyticsSerializer
    
class DeliveryAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAnalytics.objects.all()
    serializer_class = DeliveryAnalyticsSerializer
    
class RestaurantAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = RestaurantAnalytics.objects.all()
    serializer_class = RestaurantAnalyticsSerializer
    
class PopularItemAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = PopularItemAnalytics.objects.all()
    serializer_class = PopularItemAnalyticsSerializer
    
    
    
router = DefaultRouter()
router.register('order-analytics', OrderAnalyticsViewSet, 'order-analytics')
router.register('review-analytics', ReviewAnalyticsViewSet, 'review-analytics')
router.register('vendor-analytics', VendorAnalyticsViewSet, 'vendor-analytics')
router.register('revenue-analytics', RevenueAnalyticsViewSet, 'revenue-analytics')
router.register('customer-analytics', CustomerAnalyticsViewSet, 'customer-analytics')
router.register('delivery-analytics', DeliveryAnalyticsViewSet, 'delivery-analytics')
router.register('restaurant-analytics', RestaurantAnalyticsViewSet, 'restaurant-analytics')
router.register('popular-item-analytics', PopularItemAnalyticsViewSet, 'popular-item-analytics')


urlpatterns = [
    path('', include('routers.urls'))
]
    