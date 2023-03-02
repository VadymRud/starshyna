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

    # for invoice in invoices:
    #     items = invoice.items
    #     for item in items:
    #         if item['ammunition']['ammunition'] in count_amm:
    #             count_amm.update({item['ammunition']['ammunition']: item.get('quantity') + count_amm.get(
    #                 item['ammunition']['ammunition'])})
    #         else:
    #             count_amm.update({item['ammunition']['ammunition']: item.get('quantity')})



class SoldierInvoicesView(View):
    template_name = 'report/soldier_invoices.html'

    def get(self, request, id, *args, **kwargs):
        return render(request, self.template_name, {'id': id})
