from rest_framework import serializers
from gunwarehouse.models import Ammunition, Invoice, Service, Consignee, Consignor, ResponsibleRecipient, GunWarehouse


class GunWarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GunWarehouse
        fields = '__all__'


class AmmunitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ammunition
        fields = '__all__'


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ConsigneeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consignee
        fields = '__all__'


class ConsignorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consignor
        fields = '__all__'


class ResponsibleRecipientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResponsibleRecipient
        fields = '__all__'


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    gun_warehouse = GunWarehouseSerializer()
    service = ServiceSerializer()
    consignor = ConsignorSerializer()
    consignee = ConsigneeSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'
