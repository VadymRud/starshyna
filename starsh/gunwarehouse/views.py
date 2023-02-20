from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .models import (Ammunition, Invoice, Service, Consignee, Consignor, ResponsibleRecipient, GunWarehouse)
from api.gunwarehouse.serializers import (GunWarehouseSerializer, AmmunitionSerializer, ServiceSerializer,
                                          ConsigneeSerializer, ConsignorSerializer, ResponsibleRecipientSerializer,
                                          InvoiceSerializer)


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


class ConsigneeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Consignee to be viewed or edited.
    """
    queryset = Consignee.objects.all()
    serializer_class = ConsigneeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConsignorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Service to be viewed or edited.
    """
    queryset = Consignor.objects.all()
    serializer_class = ConsignorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResponsibleRecipientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GunWarehouse to be viewed or edited.
    """
    queryset = ResponsibleRecipient.objects.all()
    serializer_class = ResponsibleRecipientSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GunWarehouse to be viewed or edited.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
