from django.shortcuts import render
from django.template.loader import render_to_string
from django_tables2 import SingleTableView, RequestConfig, MultiTableMixin
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from staff.models import Staff
from gunwarehouse.models import Invoice as gunwarehouse_invoice
from .tables import StaffTable, GunWarehouseInvoiceTable


class StaffListView(SingleTableView):
    model = Staff
    table_class = StaffTable
    template_name = 'report/staff_list.html'


# class SoldierView(View):
#
#     def get(self, request, id):
#         in_hand = gunwarehouse_invoice.objects.filter(purpose='2', responsible_recipient__id=id)
#         gunwarehouse_invoices = GunWarehouseInvoiceTable(in_hand, prefix="1-")
#         RequestConfig(request, paginate=False).configure(gunwarehouse_invoices)
#         #hhhhhhh`asedrty7895trfr5rtfy6
#         rendered = render_to_string('report/invoices.html', {'gunwarehouse_invoices': gunwarehouse_invoices})
#         return HttpResponse(rendered)


class SoldierView(MultiTableMixin, TemplateView):
    template_name = 'report/invoices.html'
    tables = None




    table_pagination = {
        'per_page': 10
    }

    def get_tables(self):
        qs = gunwarehouse_invoice.objects.filter(purpose='2', responsible_recipient__id=self.kwargs.get('id'))
        qs1 = gunwarehouse_invoice.objects.all()
        self.tables = [
            GunWarehouseInvoiceTable(qs),
            GunWarehouseInvoiceTable(qs1)
        ]
        return self.tables
