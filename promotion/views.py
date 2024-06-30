from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PromotionUsageViewSet(viewsets.ModelViewSet):
    queryset = PromotionUsage.objects.all()
    serializer_class = PromotionUsageSerializer

class PromotionTagViewSet(viewsets.ModelViewSet):
    queryset = PromotionTag.objects.all()
    serializer_class = PromotionTagSerializer



router = DefaultRouter()
router.register('promo', PromotionViewSet, 'promo')
router.register('promo-usage', PromotionUsageViewSet, 'promo-usage')
router.register('promo-tag', PromotionTagViewSet, 'promo-tag')


urlpatterns = [
    path('', include(router.urls))
]
