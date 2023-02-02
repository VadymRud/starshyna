from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


#FileUpload
class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = FileUpload
        fields = ('file',)
