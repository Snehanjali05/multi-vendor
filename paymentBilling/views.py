from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class PaymentTransactionViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
    
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
class BillingAddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    
class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    
    
router = DefaultRouter()
router.register('payment-transac', PaymentTransactionViewSet, 'payment-transac')
router.register('pay-invoice', InvoiceViewSet, 'invoice')
router.register('pay-billing-addr', BillingAddressViewSet, 'billing-addr')
router.register('pay-refund', RefundViewSet, 'pay-refund' )
    
urlpatterns = [
    path('', include('router.urls'))
]