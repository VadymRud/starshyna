from django.conf import settings
from django.urls import include, path
from .views import ServiseIDListView, RegionViewSet, FileUploadViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'files', FileUploadViewSet)

urlpatterns = [
    path('', ServiseIDListView.as_view(), name='soldier_home'),
    path('api/', include(router.urls))
    # path('invoice/', InvoiceView.as_view(), name='doc_invoice'),
    # path('invoice/new/', NewInvoiceView.as_view(), name='new_invoice'),
]

