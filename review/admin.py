from django.contrib import admin
from .models import *

admin.site.register(Review)
admin.site.register(ReviewComment)
admin.site.register(ReviewReaction)