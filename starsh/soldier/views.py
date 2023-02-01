from django.shortcuts import render

from django_tables2 import SingleTableView

from .models import ServiseID
from .tables import ServiseIDTable


class ServiseIDListView(SingleTableView):
    model = ServiseID
    table_class = ServiseIDTable
    template_name = 'soldier/soldier.html'
