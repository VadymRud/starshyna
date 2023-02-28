from rest_framework import viewsets
from rest_framework import permissions

from .models import (SHPK, Staff,  Battalion, Company, Platoon, Squad)
from api.staff.serializers import (SHPKSerializer, StaffSerializer, BattalionSerializer, CompanySerializer,
                                   PlatoonSerializer, SquadSerializer)





