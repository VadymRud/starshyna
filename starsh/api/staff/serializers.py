from rest_framework import serializers
from staff.models import (SHPK, Staff,  Battalion, Company, Platoon, Squad)


class SHPKSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SHPK
        fields = '__all__'





class BattalionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Battalion
        fields = '__all__'


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PlatoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platoon
        fields = '__all__'


class PlatoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platoon
        fields = '__all__'


class SquadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Squad
        fields = '__all__'


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
