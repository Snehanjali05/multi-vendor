from django.contrib import admin
from .models import *

admin.site.register(Content)
admin.site.register(ContentCategory)
admin.site.register(ContentTag)
admin.site.register(ContentComment)
admin.site.register(ContentMedia)
admin.site.register(ContentRating)