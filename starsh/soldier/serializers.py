from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


class MilitaryRankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MilitaryRank
        fields = ['name', 'short_name']


class PlatoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platoon
        fields = ['name', 'priorety']


#Unit
class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ['name']


#FileUpload
class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = FileUpload
        fields = ('file', 'name')

