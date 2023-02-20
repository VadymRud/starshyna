from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from gunwarehouse.views import (GunWarehouseViewSet, AmmunitionViewSet, ServiceViewSet, ConsigneeViewSet,
                                ConsignorViewSet, ResponsibleRecipientViewSet, InvoiceViewSet)

router = routers.DefaultRouter()
router.register(r'gunwarehouses', GunWarehouseViewSet)
router.register(r'ammunitions', AmmunitionViewSet)
router.register(r'servises', ServiceViewSet)
router.register(r'consignee', ConsigneeViewSet)
router.register(r'consignor', ConsignorViewSet)
router.register(r'responsible_recipient', ResponsibleRecipientViewSet)
router.register(r'invoices', InvoiceViewSet)
urlpatterns = [

    path('api/', include(router.urls)),

]
