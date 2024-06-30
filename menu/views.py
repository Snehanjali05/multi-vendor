from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class MenuItemImageViewSet(viewsets.ModelViewSet):
    queryset = MenuItemImage.objects.all()
    serializer_class = MenuItemImageSerializer
    
    

router = DefaultRouter()
router.register('menu', MenuViewSet, 'menu')
router.register('menu-category', MenuCategoryViewSet, 'menu-category')
router.register('menu-item', MenuItemViewSet, 'menu-item')
router.register('menu-item-image', MenuItemImageViewSet, 'menu-item-image')

urlpatterns = [
    path('', include(router.urls))
]


urlpatterns = [
    path('', include(router.urls))
]