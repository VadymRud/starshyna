from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from gunwarehouse.views import (GunWarehouseViewSet, AmmunitionViewSet, ServiceViewSet)

router = routers.DefaultRouter()
router.register(r'regions', GunWarehouseViewSet)
router.register(r'files', AmmunitionViewSet)
router.register(r'military_ranks', ServiceViewSet)

urlpatterns = [

    path('api/', include(router.urls)),

]
