from django.db import models
import uuid
from users.models import User, CustomerProfile
from enum import Enum

class status_type(Enum):
    DRAFT = 'draft'
    PUBLISHED = 'publish'
    ARCHIEVED = 'archieved'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]
    
class content_type_choice(Enum):
    ARTICLE = 'article'
    BLOG = 'blog'
    PAGE = 'page'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]

class content_comment_choice(Enum):
    APPROVED = 'approved'
    PENDING = 'pending'
    REJECTED = 'rejected'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]

class media_type_choice(Enum):
    IMAGE = 'image'
    VIDEO = 'video'
    DOCUMENT = 'document'
    
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]



class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)  
    body = models.TextField()  
    author = models.ForeignKey(User, on_delete=models.PROTECT) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    published_at = models.DateTimeField(null=True, blank=True)  
    status = models.CharField(choices=status_type.choices(), max_length=16) 
    content_type = models.CharField(choices=content_type_choice.choices(), max_length=8) 
    
    def __str__(self):
        return self.title

class ContentCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128) 
    description = models.TextField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.name


class ContentTag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name

class ContentComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content_id  = models.ForeignKey(Content, on_delete=models.PROTECT) 
    author_id  = models.ForeignKey(User, on_delete=models.PROTECT)  
    body = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=content_comment_choice.choices(), max_length=8) 

    def __str__(self):
        return f"{self.author_id} - {self.content_id}"

class ContentMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content_id = models.ForeignKey(Content, on_delete=models.PROTECT)
    media_file = models.FileField(upload_to='content_media/') 
    media_type = models.CharField(choices=media_type_choice.choices(), max_length=8)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.media_type} - {self.content_id.title}"

class ContentRating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content_id = models.ForeignKey(Content, on_delete=models.PROTECT)
    user_id = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT) 
    rating = models.PositiveSmallIntegerField()  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.content_id.title} - {self.rating}"