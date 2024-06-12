from django.contrib import admin
from .models import *

admin.site.register(LoyaltyProgram)
admin.site.register(LoyaltyMember)
admin.site.register(LoyaltyTransaction)
admin.site.register(Reward)
admin.site.register(Redemption)