from django.contrib import admin

from django.utils.translation import gettext as _
from .models import (SHPK, Staff, Name, Kontrakt, PosadaName, Shtatka, ZvannyaName, OsvitaName,
                     StatsName, StatusName, PidrozdilName, Battalion, Company, Platoon, Squad)

admin.site.register(SHPK)
admin.site.register(Staff)
admin.site.register(Name)
admin.site.register(Kontrakt)
admin.site.register(PosadaName)
admin.site.register(Shtatka)
admin.site.register(ZvannyaName)
admin.site.register(OsvitaName)
admin.site.register(StatsName)
admin.site.register(StatusName)
admin.site.register(PidrozdilName)
admin.site.register(Battalion)
admin.site.register(Company)
admin.site.register(Platoon)
admin.site.register(Squad)
