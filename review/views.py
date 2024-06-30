from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review
    serializer_class = ReviewSerializer
    
class ReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = ReviewComment
    serializer_class = ReviewCommentSerializer
    
class ReviewReactionViewSet(viewsets.ModelViewSet):
    queryset = ReviewReaction
    serializer_class = ReviewReactionSerializer
    
    
router = DefaultRouter()
router.register('review', ReviewViewSet, 'review')
router.register('review-comment', ReviewCommentViewSet, 'review-comment')
router.register('review-reaction', ReviewReactionViewSet, 'review-reaction')

urlpatterns = [
    path('', include(router.urls))
]
