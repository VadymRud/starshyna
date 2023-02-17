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



