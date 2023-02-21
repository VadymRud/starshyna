from django.contrib import admin

from django.utils.translation import gettext as _
from .models import (SHPK, Staff,  Battalion, Company, Platoon, Squad)

admin.site.register(SHPK)
admin.site.register(Staff)
admin.site.register(Battalion)
admin.site.register(Company)
admin.site.register(Platoon)
admin.site.register(Squad)
