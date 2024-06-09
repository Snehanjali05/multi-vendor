from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class RestaurantCategoryViewSet(viewsets.ModelViewSet):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer
    
class RestaurantPhotoViewSet(viewsets.ModelViewSet):
    queryset = RestaurantPhoto.objects.all()
    serializer_class = RestaurantPhotoSerializer
    
class RestaurantHoursViewSet(viewsets.ModelViewSet):
    queryset = RestaurantHours.objects.all()
    serializer_class = RestaurantHoursSerializer
    
class RestaurantRevenueViewSet(viewsets.ModelViewSet):
    queryset = RestaurantRevenue.objects.all()
    serializer_class = RestaurantRevenueSerializer
    
    
router = DefaultRouter()
router.register('restaurant', RestaurantViewSet, 'restaurant')
router.register('restaurant-category', RestaurantCategoryViewSet, 'restaurant-category')
router.register('restaurant-photo', RestaurantPhotoViewSet, 'restaurant-photo')
router.register('restaurant-revenue', RestaurantRevenueViewSet, 'restaurant-revenue')
router.register('restaurant-hours', RestaurantHoursViewSet, 'restaurant-hours')


urlpatterns = [
    path('', include(router.urls))
]