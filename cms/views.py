from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
class ContentCategoryViewSet(viewsets.ModelViewSet):
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer
    
class ContentTagViewSet(viewsets.ModelViewSet):
    queryset = ContentTag.objects.all()
    serializer_class = ContentTagSerializer
    
class ContentCommentViewSet(viewsets.ModelViewSet):
    queryset = ContentComment.objects.all()
    serializer_class = ContentCommentSerializer
    
class ContentMediaViewSet(viewsets.ModelViewSet):
    queryset = ContentMedia.objects.all()
    serializer_class = ContentMediaSerializer
    
class ContentRatingViewSet(viewsets.ModelViewSet):
    queryset = ContentRating.objects.all()
    serializer_class = ContentRatingSerializer
    
    
router = DefaultRouter()
router.register('content', ContentViewSet, 'content')
router.register('content-category', ContentCategoryViewSet, 'content-category')
router.register('content-tag', ContentTagViewSet, 'content-tag')
router.register('content-comment', ContentCommentViewSet, 'content-comment')
router.register('content-media', ContentMediaViewSet, 'content-media')
router.register('content-rating', ContentRatingViewSet, 'content-rating')

urlpatterns = [
    path('', include(router.urls))
]
