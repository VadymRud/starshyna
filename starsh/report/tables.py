import django_tables2 as tables
from django_tables2.utils import A
from staff.models import Staff
from gunwarehouse.models import Invoice as gunwarehouse_invoice


class StaffTable(tables.Table):
    #edit = tables.LinkColumn('staff', args=[A('pk')])
    detail = tables.LinkColumn('soldier', text=lambda record: record.name, args=[A('pk')])
    class Meta:
        model = Staff
        template_name = 'django_tables2/bootstrap.html'
        fields = ('pk', 'name', 'ocoba.military_ranks', 'ocoba.name', 'ocoba.sename',)


class GunWarehouseInvoiceTable(tables.Table):
    # edit = tables.LinkColumn('staff', args=[A('pk')])

    class Meta:
        model = gunwarehouse_invoice
        template_name = 'django_tables2/bootstrap.html'
        fields = ('pk', 'gun_warehouse.name', 'number', 'ocoba.name', 'ocoba.sename',)
