from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Users/', include('users.views')),
    path('Restaurant/', include('restaurant.views')),
    path('Menu/', include('menu.views')),
    path('Order/', include('order.views')),
    path('Delivery/', include('delivery.views')),    
]
