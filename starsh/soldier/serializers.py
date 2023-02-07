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


#Company
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['unik', 'name', 'short_name']


#Creed
class CreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creed
        fields = ['name']


#Nationality
class NationalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nationality
        fields = ['name']


#Education
class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ['name']


#State
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['name']


#OfficialPosition
class OfficialPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfficialPosition
        fields = ['name']


#ServiseID
class ServiseIDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiseID
        fields = '__all__'

#FileUpload
class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = FileUpload
        fields = ('file', 'name')

