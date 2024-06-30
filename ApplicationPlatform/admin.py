from django.contrib import admin
from .models import *

admin.site.register(PlatformAnalytic)
admin.site.register(PlatformNotification)
admin.site.register(PlatformFeedback)
admin.site.register(PlatformAdminLog)