from django.contrib import admin
from .models import *

admin.site.register(Delivery)
admin.site.register(DeliveryVehicle)
admin.site.register(DeliveryFeedback)
admin.site.register(DeliveryHistory)