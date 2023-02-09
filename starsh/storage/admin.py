from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Storage, Invoice

admin.site.register(Storage)
admin.site.register(Invoice)

