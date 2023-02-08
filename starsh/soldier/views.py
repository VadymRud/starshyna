from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django_tables2 import SingleTableView
from .models import (Region, FileUpload, MilitaryRank, Platoon, Unit, Company, Creed, Nationality,
                     Education, State, OfficialPosition, ServiseID, BattleWound, Reward)
from .tables import ServiseIDTable
from .serializers import (RegionSerializer, FileUploadSerializer, MilitaryRankSerializer, PlatoonSerializer,
                          UnitSerializer, CompanySerializer, CreedSerializer, NationalitySerializer,
                          EducationSerializer, StateSerializer, OfficialPositionSerializer, ServiseIDSerializer,
                          BattleWoundSerializer, RewardSerializer)
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


class PlatoonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed or edited.
    """
    queryset = Platoon.objects.all()
    serializer_class = PlatoonSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Company to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class CreedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Creed to be viewed or edited.
    """
    queryset = Creed.objects.all()
    serializer_class = CreedSerializer
    permission_classes = [permissions.IsAuthenticated]


class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Unit to be viewed or edited.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]


class OfficialPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OfficialPosition to be viewed or edited.
    """
    queryset = OfficialPosition.objects.all()
    serializer_class = OfficialPositionSerializer
    permission_classes = [permissions.IsAuthenticated]


class NationalityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Nationality to be viewed or edited.
    """
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
    permission_classes = [permissions.IsAuthenticated]


class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Education to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]


class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows State to be viewed or edited.
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]


class OfficialPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OfficialPosition to be viewed or edited.
    """
    queryset = OfficialPosition.objects.all()
    serializer_class = OfficialPositionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiseIDViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ServiseID to be viewed or edited.
    """
    queryset = ServiseID.objects.all()
    serializer_class = ServiseIDSerializer
    permission_classes = [permissions.IsAuthenticated]


class BattleWoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BattleWound to be viewed or edited.
    """
    queryset = BattleWound.objects.all()
    serializer_class = BattleWoundSerializer
    permission_classes = [permissions.IsAuthenticated]


class RewardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Reward to be viewed or edited.
    """
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
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