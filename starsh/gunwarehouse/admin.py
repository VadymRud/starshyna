from django.contrib import admin
from .models import Ammunition, Invoice, Service
# Register your models here.


admin.site.register(Ammunition)
admin.site.register(Service)
admin.site.register(Invoice)
