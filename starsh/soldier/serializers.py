from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from staff.models import Staff


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'id']


class MilitaryRankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MilitaryRank
        fields = ['name', 'short_name']


class PlatoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platoon
        fields = ['name', 'priorety']


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ['name']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['unik', 'name', 'short_name']


class CreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creed
        fields = ['name']


class NationalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nationality
        fields = ['name']


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ['name']


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['name']


class OfficialPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfficialPosition
        fields = ['name']


class BattleWoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BattleWound
        fields = '__all__'


class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'


class ServiseIDSerializer(serializers.HyperlinkedModelSerializer):
    military_ranks = MilitaryRankSerializer()
    creed = CreedSerializer()
    nationality = NationalitySerializer()
    education = EducationSerializer()
    state_pr = StateSerializer()
    region_pr = RegionSerializer()
    state_fact = StateSerializer()
    region_fact = RegionSerializer()
    battle_wound = BattleWoundSerializer(many=True)
    award = AwardSerializer(many=True)

    class Meta:
        model = ServiseID
        fields = '__all__'


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = FileUpload
        fields = ('file', 'name')

