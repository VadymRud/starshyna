from django.db import models
from django.utils.translation import gettext as _
from django_jsonform.models.fields import JSONField
from django.utils import timezone
from soldier.models import ServiseID


class GunWarehouse(models.Model):
    # Склад БК
    full_name = models.CharField(max_length=512, verbose_name=_('Full name'))
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Gun Warehouse')
        verbose_name_plural = _('Gun Warehouses')


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
    purposes = [
        ('1', _('Arrived')),
        ('2', _('Out')),
    ]

    goods = [
        ('1', _('Ammunition')),
        ('2', _('Gun')),
        ('3', _('Devises')),
    ]

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

          "quantity": {
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
    gun_warehouse = models.ForeignKey(GunWarehouse, verbose_name=_('Gun Warehouse'), on_delete=models.CASCADE,
                                      null=True, blank=True)

    number = models.CharField(verbose_name=_('Number'), max_length=50)
    purpose = models.CharField(verbose_name=_('Purpose'), choices=purposes, default='2', max_length=50)
    good_class = models.CharField(verbose_name=_('Good class'), choices=goods, default='2', max_length=50)
    date_created = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name=_('Date created'))
    service = models.ForeignKey(Service, verbose_name=_('Service'), on_delete=models.CASCADE, null=True, blank=True)
    consignor = models.ForeignKey(Consignor, verbose_name=_('Consignor'), on_delete=models.CASCADE, null=True,
                                  blank=True)
    consignee = models.ForeignKey(Consignee, verbose_name=_('Consignee'), on_delete=models.CASCADE, null=True,
                                  blank=True)
    responsible_recipient = models.ForeignKey(ServiseID, verbose_name=_('ResponsibleRecipient'),
                                              on_delete=models.CASCADE, null=True, blank=True)
    items = JSONField(schema=ITEMS_SCHEMA)

    def __str__(self):
        return '{pk} {number}'.format(pk=self.pk, number=self.number)

    def save(self, *args, **kwargs):
        self.number = "{pk}/{good_class}".format(pk=self.pk, good_class=self.goods[int(self.good_class)-1][1])
        super(Invoice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')


class Weapon(models.Model):
    type_weapons = [
        ('1', _('Pistol')),
        ('2', _('Rifle')),
        ('3', _('Machinegun')),
        ('4', _('Grenade launcher')),
        ('5', _('Sniper rifle')),
        ('6', _('Large-caliber weapon')),
    ]

    type_issued = [
        (1, _('Not issued')),
        (2, _('Issued')),
        (3, _('Miss')),

    ]

    ITEMS_SCHEMA = {
        "type": "object",
        "title": _("Attributes"),
        "keys": {

            "Additional properties": {
                "type": "string"
            }
        },
        "additionalProperties": {
            "type": "string"
        }
    }
    type_weapon = models.CharField(verbose_name=_('Type Weapon'), choices=type_weapons, default=1, max_length=50)
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    calibre = models.CharField(verbose_name=_('Calibre'),  max_length=50)
    serial_number = models.CharField(verbose_name=_('Serial number'),  max_length=256)
    issued = models.PositiveSmallIntegerField(verbose_name=_('Issued'), choices=type_issued, default=1)
    additional = JSONField(schema=ITEMS_SCHEMA, blank=True, null=True)

    def __str__(self):
        return '{pk} {name} {serial}'.format(pk=self.pk, name=self.name, serial=self.serial_number)

    class Meta:
        verbose_name = _('Weapon')
        verbose_name_plural = _('Weapons')


class InvoiceWeapon(models.Model):
    purposes = [
        ('1', _('Arrived')),
        ('2', _('Out')),
    ]

    weaps = Weapon.objects.all()
    choices = []
    lis = {}
    for weap in weaps:
        text_status = weap.type_issued[weap.issued-1][1]
        text_title = '{name} {serial} {status}'.format(name=weap.name, serial=weap.serial_number, status=text_status)
        lis = {'title': text_title, 'value': weap.pk}
        choices.append(lis)


    ITEMS_SCHEMA = {
      "type": "array",
      "items": {
        "type": "object",
        "title": _("Quantity"),
        "keys": {
          "weapon": {
              "type": "object",
              "keys": {
                  "weapon": {
                      "type": "string",
                      "choices": choices
                  }
              }
          }
        }
      }
    }
    gun_warehouse = models.ForeignKey(GunWarehouse, verbose_name=_('Gun Warehouse'), on_delete=models.CASCADE,
                                      null=True, blank=True)
    number = models.CharField(verbose_name=_('Number'), max_length=50)
    purpose = models.CharField(verbose_name=_('Purpose'), choices=purposes, default='2', max_length=50)
    date_created = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name=_('Date created'))
    responsible_recipient = models.ForeignKey(ServiseID, verbose_name=_('ResponsibleRecipient'),
                                              on_delete=models.CASCADE, null=True, blank=True)
    weapons = JSONField(schema=ITEMS_SCHEMA)

    def __str__(self):
        return '{pk} {number}'.format(pk=self.pk, number=self.number)

    def save(self, *args, **kwargs):
        self.number = "{pk}/{good_class}".format(pk=self.pk, good_class=_('Weapon'))

        for weap in self.weapons:
            w = Weapon.objects.get(pk=weap.get('weapon').get('weapon'))
            if self.purpose == '2':
                w.issued = 2
                w.save()
            else:
                w.issued = 1
                w.save()
        super(InvoiceWeapon, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Invoice Weapon')
        verbose_name_plural = _('Invoice Weapons')
