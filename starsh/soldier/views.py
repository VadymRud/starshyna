from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django_tables2 import SingleTableView

from .models import ServiseID, Region
from .tables import ServiseIDTable
from .serializers import RegionSerializer


class ServiseIDListView(SingleTableView):
    model = ServiseID
    table_class = ServiseIDTable
    template_name = 'soldier/soldier.html'


class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows regions to be viewed or edited.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]


