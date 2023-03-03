from django.contrib import admin
from .models import (Ammunition, Invoice, Service, Consignee, Consignor, ResponsibleRecipient, GunWarehouse, Weapon,
                     InvoiceWeapon)
# Register your models here.


admin.site.register(GunWarehouse)
admin.site.register(Ammunition)
admin.site.register(Service)
admin.site.register(Consignor)
admin.site.register(Consignee)
admin.site.register(ResponsibleRecipient)
admin.site.register(Invoice)
admin.site.register(Weapon)
admin.site.register(InvoiceWeapon)
