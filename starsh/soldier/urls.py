from django.conf import settings
from django.urls import include, path
from .views import ServiseIDListView

urlpatterns = [
    path('', ServiseIDListView.as_view(), name='soldier_home'),
    # path('invoice/', InvoiceView.as_view(), name='doc_invoice'),
    # path('invoice/new/', NewInvoiceView.as_view(), name='new_invoice'),
]

