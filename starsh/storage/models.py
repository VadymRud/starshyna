from django.db import models
from django.utils.translation import gettext as _
from django_jsonform.models.fields import JSONField


class Storage(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    priorety = models.SmallIntegerField(verbose_name=_('Name'), default=1)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Storage')
        verbose_name_plural = _('Storage')


class Invoice(models.Model):
    choices = [
                  "New york",
                  "London",
                  "Mumbai",
                  "Tokyo"
                ]

    ITEMS_SCHEMA = {
      "type": "array",
      "items": {
        "type": "object",
        "title": _("Person"),
        "keys": {
          _("name"): {
            "type": "string"
          },
          _("age"): {
            "type": "integer"
          },
          "autocompliet": {
              "type": "array",
              "title": "Cities",
              "items": {
                "type": "string",
                "choices": choices,
                "widget": "multiselect"
              }
          }
        }
      }
    }
    items = JSONField(schema=ITEMS_SCHEMA)
    date_created = models.DateTimeField(auto_now_add=True)
