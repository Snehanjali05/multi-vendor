from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Users/', include('users.views')),
    path('Restaurant/', include('restaurant.views')),
    path('Menu/', include('menu.views')),
    path('Order/', include('order.views')),
    path('Delivery/', include('delivery.views')),   
    path('Review/', include('review.views')),
    path('Promotion/', include('promotion.views')),
    path('Notification/', include('notification.views')), 
    path('Analytics/', include('analytics.views')), 
    path('Inventory/', include('inventory.views')),
    path('Subscription/', include('subscription.views')),
    path('Loyalty/', include('loyalty.views')),
    path('PaymentBilling/', include('paymentBilling.views')),
    path('Cms/', include('cms.views')),
    path('ApplicationPlatform/', include('ApplicationPlatform.views')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
