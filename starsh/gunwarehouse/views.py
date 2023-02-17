from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .models import (Ammunition, Invoice, Service, Consignee, Consignor, ResponsibleRecipient, GunWarehouse)
from api.gunwarehouse.serializers import (GunWarehouseSerializer, AmmunitionSerializer, ServiceSerializer)


class AmmunitionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ammunition to be viewed or edited.
    """
    queryset = Ammunition.objects.all()
    serializer_class = AmmunitionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Service to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class GunWarehouseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GunWarehouse to be viewed or edited.
    """
    queryset = GunWarehouse.objects.all()
    serializer_class = GunWarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]
