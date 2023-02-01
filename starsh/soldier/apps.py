from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SoldierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soldier'
    verbose_name = _('Persons')
