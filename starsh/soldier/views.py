from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django_tables2 import SingleTableView
from .models import ServiseID, Region, FileUpload, MilitaryRank, Platoon, Unit
from .tables import ServiseIDTable
from .serializers import (RegionSerializer, FileUploadSerializer, MilitaryRankSerializer, PlatoonSerializer,
                          UnitSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class ServiseIDListView(SingleTableView):
    model = ServiseID
    table_class = ServiseIDTable
    template_name = 'soldier/soldier.html'


class MilitaryRankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Military Rank to be viewed or edited.
    """
    queryset = MilitaryRank.objects.all()
    serializer_class = MilitaryRankSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]


#Platoon
class PlatoonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed or edited.
    """
    queryset = Platoon.objects.all()
    serializer_class = PlatoonSerializer
    permission_classes = [permissions.IsAuthenticated]


class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Unit to be viewed or edited.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]




class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = [
        permissions.AllowAny]

    def pre_save(self, obj):
        obj.samplesheet = self.request.FILES.get('file')


class CustomAuthToken(ObtainAuthToken):

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })