from django.conf import settings
from django.urls import include, path
from .views import (ServiseIDListView, RegionViewSet, FileUploadViewSet, CustomAuthToken, MilitaryRankViewSet,
                    PlatoonViewSet, UnitViewSet, CompanyViewSet, NationalityViewSet, EducationViewSet, StateViewSet,
                    OfficialPositionViewSet, ServiseIDViewSet, BattleWoundViewSet, AwardViewSet)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'files', FileUploadViewSet)
router.register(r'military_ranks', MilitaryRankViewSet)
router.register(r'platoons', PlatoonViewSet)
router.register(r'units', UnitViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'nationalities', NationalityViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'states', StateViewSet)
router.register(r'officialpositions', OfficialPositionViewSet)
router.register(r'soldiers', ServiseIDViewSet)
router.register(r'battle_wounds', BattleWoundViewSet)
router.register(r'award', AwardViewSet)
#router.register(r'sold_auth', UserAuthificateView)

urlpatterns = [
    path('', ServiseIDListView.as_view(), name='soldier_home'),
    path('api/', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view())
    # path('invoice/', InvoiceView.as_view(), name='doc_invoice'),
    # path('invoice/new/', NewInvoiceView.as_view(), name='new_invoice'),
]

