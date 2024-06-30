from django.contrib import admin
from .models import *

admin.site.register(PaymentTransaction)
admin.site.register(Invoice)
admin.site.register(BillingAddress)
admin.site.register(Refund)