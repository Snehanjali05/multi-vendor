from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(RestaurantCategory)
admin.site.register(RestaurantPhoto)
admin.site.register(RestaurantRevenue)
admin.site.register(RestaurantHours)