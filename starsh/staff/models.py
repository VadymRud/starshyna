from django.db import models

from django.utils.translation import gettext as _
from soldier.models import ServiseID, Company


class SHPK(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    short_name = models.CharField(max_length=512, verbose_name=_('Short name'), blank=True, null=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('SHPK')
        verbose_name_plural = _('SHPK')


class Zvannya(models.Model):
    zv_id = models.AutoField(primary_key=True)
    zv_name = models.TextField()
    zv_short_name = models.CharField(max_length=20)

    def __str__(self):
        return '{}__{}'.format(self.zv_id, self.zv_name)

    class Meta:
        managed = False
        db_table = 'zvannya_name'


class Battalion(models.Model):
    unicum = models.CharField(verbose_name=_('Unic number'), null=True, blank=True, max_length=100)
    name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=1024)
    short_name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=100)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _('Battalion')
        verbose_name_plural = _('Battalions')


class Company(models.Model):
    # рота
    unicum = models.CharField(verbose_name=_('Unic number'), null=True, blank=True, max_length=100)
    name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=1024)
    short_name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=100)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class Platoon(models.Model):
    # взвод
    unicum = models.CharField(verbose_name=_('Unic number'), null=True, blank=True, max_length=100)
    name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=1024)
    short_name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=100)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _('Platoon')
        verbose_name_plural = _('Platoons')


class Squad(models.Model):
    # відділення
    unicum = models.CharField(verbose_name=_('Unic number'), null=True, blank=True, max_length=100)
    name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=1024)
    short_name = models.CharField(verbose_name=_('name'), null=True, blank=True, max_length=100)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _('Squad')
        verbose_name_plural = _('Squads')


class Staff(models.Model):
    # Штатка
    #порядковий номер в штатці
    unicum = models.PositiveBigIntegerField(verbose_name=_('Unic number'), null=True, blank=True)
    battalion = models.ForeignKey(Battalion, on_delete=models.CASCADE, blank=True, verbose_name=_('Battalion'),
                                  null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, verbose_name=_('Company'), null=True)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, blank=True, verbose_name=_('Platoon'), null=True)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, blank=True, verbose_name=_('Squad'), null=True)
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    shpk = models.ForeignKey(SHPK, on_delete=models.CASCADE, blank=True, verbose_name=_('shpk'))
    ocoba = models.ForeignKey(ServiseID, on_delete=models.CASCADE, blank=True, verbose_name=_('ocoba'), null=True)
    vos = models.CharField(max_length=512, verbose_name=_('VOS'))
    poz = models.CharField(max_length=512, verbose_name=_('pozyvnyy'), blank=True)
    salary = models.PositiveBigIntegerField(verbose_name=_('salary'), blank=True, null=True, default=0)
    tariff_category = models.PositiveBigIntegerField(verbose_name=_('tariff category'), blank=True, null=True, default=0)
    vacant = models.BooleanField(verbose_name=_('Vacant'), blank=True, null=True, default=True)


    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')


