from django.db import models
from django.utils.translation import gettext as _
from django_jsonform.models.fields import JSONField
from django.utils import timezone


class Ammunition(models.Model):

    ITEMS_SCHEMA = {
          "type": "object",
          "title": _("Attributes"),
          "keys": {

            _("unit of measurement"): {
              "type": "string"
            }
          },
          "additionalProperties": {
            "type": "string"
          }
    }

    items = JSONField(schema=ITEMS_SCHEMA)
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Ammunition')
        verbose_name_plural = _('Ammunition')


class Service(models.Model):
    # Служба
    full_name = models.CharField(max_length=512, verbose_name=_('Full name'))
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')


class Consignor(models.Model):
    # Вантажовідправник
    full_name = models.CharField(max_length=512, verbose_name=_('Full name'))
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Consignor')
        verbose_name_plural = _('Consignors')


class Consignee(models.Model):
    # Вантажоотримувач
    full_name = models.CharField(max_length=512, verbose_name=_('Full name'))
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Consignee')
        verbose_name_plural = _('Consignees')


class ResponsibleRecipient(models.Model):
    # Відповідальний одержувач
    full_name = models.CharField(max_length=512, verbose_name=_('Full name'))
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Responsible Recipient')
        verbose_name_plural = _('Responsible Recipients')


class Invoice(models.Model):
    amms = Ammunition.objects.all()
    choices = []
    for amm in amms:
        lis = {'title': amm.name, 'value': amm.pk}
        choices.append(lis)

    ITEMS_SCHEMA = {
      "type": "array",
      "items": {
        "type": "object",
        "title": _("Quantity"),
        "keys": {

          _("quantity"): {
            "type": "integer"
          },
          "ammunition": {
              "type": "object",
              "keys": {
                  "ammunition": {
                      "type": "string",
                      "choices": choices
                  }
              }
          }
        }
      }
    }
    number = models.CharField(verbose_name=_('Number'), max_length=50)
    date_created = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name=_('Date created'))
    service = models.ForeignKey(Service, verbose_name=_('Service'), on_delete=models.CASCADE, null=True, blank=True)
    items = JSONField(schema=ITEMS_SCHEMA)

    def __str__(self):
        return '{pk}'.format(pk=self.pk)

    class Meta:
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')
