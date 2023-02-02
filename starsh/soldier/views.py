from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django_tables2 import SingleTableView
from .models import ServiseID, Region, FileUpload
from .tables import ServiseIDTable
from .serializers import RegionSerializer, FileUploadSerializer



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


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
