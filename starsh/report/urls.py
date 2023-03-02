from django.urls import path

from .views import StaffListView, SoldierView, SoldierInvoicesView

urlpatterns = [

    path('staff/', StaffListView.as_view(), name='full_staff'),
    path('soldier/<int:id>/', SoldierInvoicesView.as_view(), name='soldier'),
]
