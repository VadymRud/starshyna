from django.db import models
# Create your models here.
from django.utils.translation import gettext as _
from django.conf.global_settings import STATIC_ROOT
from django import forms


class MilitaryRank(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    short_name = models.CharField(max_length=512, verbose_name=_('Short name'), blank=True, null=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Military Rank')
        verbose_name_plural = _('Military Ranks')


class Platoon(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    priorety = models.SmallIntegerField(verbose_name=_('Name'), default=1)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Platoon')
        verbose_name_plural = _('Platoons')


class Unit(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')


class Company(models.Model):
    unik = models.PositiveBigIntegerField(verbose_name=_('Unic number'), blank=True)
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    short_name = models.CharField(max_length=512, verbose_name=_('Short name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Company')


class Creed(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Creed')
        verbose_name_plural = _('Creed')


class Nationality(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationalities')


class Education(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Education')


class State(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')


class Region(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')


class OfficialPosition(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    shpk = models.CharField(max_length=512, verbose_name=_('SHPK'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Official Position')
        verbose_name_plural = _('Official Positions')


def image_directory_path(instance, filename):
    return '{}/images/{}_{}_{}_{}/{}'.format('media', instance.military_ranks.name, instance.name, \
                                             instance.sename, instance.third_name, filename)


class ServiseID(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name Person'))
    sename = models.CharField(max_length=512, verbose_name=_('Sename'))
    third_name = models.CharField(max_length=512, verbose_name=_('third name'), blank=True, null=True)
    nickname = models.CharField(max_length=512, verbose_name=_('nickname'), blank=True, null=True)
    # В давальному відмінку
    name_accs = models.CharField(max_length=512, verbose_name=_('Name Person in accs'), blank=True, null=True)
    sename_accs = models.CharField(max_length=512, verbose_name=_('Sename in accs'), blank=True, null=True)
    third_name_accs = models.CharField(max_length=512, verbose_name=_('third name  in accs'), blank=True, null=True)

    birth_date = models.DateField(verbose_name=_('birth date'))
    military_ranks = models.ForeignKey(MilitaryRank, on_delete=models.CASCADE, verbose_name=_('military rank'))
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('company'))
    # platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, blank=True, verbose_name=_('platoon'), null=True)
    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, verbose_name=_('unit'), null=True)
    image3x4 = models.BinaryField(blank=True, verbose_name=_('image3x4'))
    image_face3x4 = models.ImageField(upload_to=image_directory_path, blank=True, verbose_name=_('image_face3x4'))
    # official_position = models.ForeignKey(OfficialPosition, on_delete=models.CASCADE, blank=True, verbose_name=_('official_position'))
    # інфо про призов
    military_office = models.CharField(max_length=1024, verbose_name=_('Military office'), blank=True, null=True)
    date_of_conscription = models.DateField(verbose_name=_('date of conscription'), blank=True, null=True)
    order_date = models.DateField(verbose_name=_('order date'), blank=True, null=True)
    order_number = models.CharField(max_length=100, verbose_name=_('order number'), blank=True, null=True)
    # військовий квиток
    militaryID_seria = models.CharField(max_length=3, verbose_name=_('militaryID seria'), blank=True, null=True)
    militaryID_number = models.CharField(max_length=10, verbose_name=_('militaryID number'), blank=True, null=True)
    who_militaryID = models.CharField(max_length=10, verbose_name=_('who_militaryID'), blank=True, null=True)
    militaryID_date = models.DateField(verbose_name=_('militaryID_date'), blank=True, null=True)
    weapon = models.CharField(max_length=1020, verbose_name=_('weapon'), blank=True, null=True)
    military_rank_id = models.CharField(max_length=1020, verbose_name=_('military_rank_id'), blank=True, null=True)
    military_rank_date = models.DateField(verbose_name=_('military_rank_date'), blank=True, null=True)

    # паспорт
    ID_seria = models.CharField(max_length=3, verbose_name=_('ID seria'), blank=True, null=True)
    ID_number = models.CharField(max_length=10, verbose_name=_('ID number'), blank=True, null=True)
    who_ID = models.CharField(max_length=10, verbose_name=_('who_ID'), blank=True, null=True)
    ID_date = models.DateField(verbose_name=_('ID_date'), blank=True, null=True)
    ipn = models.CharField(max_length=10, verbose_name=_('ipn'), blank=True, null=True)

    # загальна інформація
    orphan = models.BooleanField(_('orphan'), default=False, help_text=_('orphan'))
    married = models.BooleanField(_('married'), default=False)
    halforphan = models.BooleanField(_('halforphan'), default=False)
    work = models.BooleanField(_('work'), default=False)
    mobilization = models.BooleanField(_('mobilization'), default=False)
    driveid = models.BooleanField(_('driveid'), default=False)
    driveid_category = models.CharField(max_length=100, verbose_name=_('driveid category'), blank=True, null=True)
    creed = models.ForeignKey(Creed, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('creed'))
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name=_('nationality'))
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name=_('Education'))
    blood_type = models.CharField(max_length=3, verbose_name=_('blood_type'), blank=True, null=True)
    rh = models.CharField(max_length=2, verbose_name=_('RH'), blank=True, null=True)
    # адреси проживання
    # прописка
    state_pr = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('state'),
                                 related_name='+')
    region_pr = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('region'),
                                  related_name='+')
    addres_pr = models.TextField(verbose_name=_('addres_pr'), blank=True, null=True)
    postal_code_pr = models.CharField(max_length=25, verbose_name=_('postal code_pr'), blank=True, null=True)
    # фактична
    state_fact = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('state fact'),
                                   related_name='+')
    region_fact = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name=_('region fact'), related_name='+')
    addres_fact = models.TextField(verbose_name=_('address fact'), blank=True, null=True)
    postal_code_fact = models.CharField(max_length=25, verbose_name=_('postal code'), blank=True, null=True)
    phone1 = models.CharField(max_length=25, verbose_name=_('phone home'), blank=True, null=True)
    phone2 = models.CharField(max_length=25, verbose_name=_('phone mobile'), blank=True, null=True)
    father = models.CharField(max_length=500, verbose_name=_('father'), blank=True, null=True)
    mother = models.CharField(max_length=500, verbose_name=_('mother'), blank=True, null=True)
    partner = models.CharField(max_length=500, verbose_name=_('partner'), blank=True, null=True)

    def __str__(self):
        return '{} {} {} {}'.format(str(self.military_ranks.name), str.upper(self.sename), str(self.name),
                                    str(self.third_name))

    class Meta:
        verbose_name = _('ServiseID')
        verbose_name_plural = _('ServiseIDs')


class Command(models.Model):
    CHOICES = (
        ('KB', _('Battalion commander')),
        ('ZKB', _('Deputy Battalion Commander')),
        ('ZKBMPZ', _('Deputy Battalion Commander for Moral and Psychological Support')),
        ('PKBZPR', _('Assistant Battalion Commander for Legal Affairs')),
        ('OP', _('Officer-psychologist')),
        ('GSVCH', _('Chief sergeant of a military unit')),
        ('Tehnic', _('Technician')),
        ('ZKBPDP', _('Deputy Battalion Commander for Airborne Training')),
        ('ZKBNSH', _('Chief of Staff - First Deputy Battalion Commander')),
        ('SPZKISCH', _('Senior assistant chief of staff for personnel and military units')),
    )
    name = models.CharField(max_length=512, choices=CHOICES, verbose_name=_('Name Command'))
    person = models.ForeignKey(ServiseID, on_delete=models.CASCADE, verbose_name=_('Name Person'))
    temporarily = models.PositiveSmallIntegerField(default=0, verbose_name=_('TVO'))

    def __str__(self):
        return '{} {} {} {}'.format(str(self.get_name_display()), str(self.person.name),
                                    str(self.person.sename), str(self.person.third_name))

    class Meta:
        verbose_name = _('Command')
        verbose_name_plural = _('Commands')


def file_upload_to_directory(instance, filename):
    return '/'.join(['media', 'temporary', filename])


class FileUpload(models.Model):
    file = models.FileField(upload_to=file_upload_to_directory, blank=True, null=True, default='')
