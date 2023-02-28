from django.urls import path

from .views import StaffListView, SoldierView

urlpatterns = [

    path('staff/', StaffListView.as_view(), name='full_staff'),
    path('soldier/<int:id>/', SoldierView.as_view(), name='soldier'),

]