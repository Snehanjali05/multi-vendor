from rest_framework import serializers
from .models import *

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
        
class ContentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCategory
        fields = '__all__'
        
class ContentTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTag
        fields = '__all__'

class ContentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentComment
        fields = '__all__'
        
class ContentMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentMedia
        fields = '__all__'
        
class ContentRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentRating
        fields = '__all__'