from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GunwarehouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gunwarehouse'
    verbose_name = _('Gun warehouses')
