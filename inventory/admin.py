from django.contrib import admin
from .models import *

admin.site.register(InventoryCategory)
admin.site.register(InventoryItem)
admin.site.register(InventoryStock)
admin.site.register(InventorySupplier)
admin.site.register(InventoryOrder)
admin.site.register(InventoryOrderItem)