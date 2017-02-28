from __future__ import unicode_literals

from django.db import models
from smart_selects.db_fields import ChainedForeignKey
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from colorful.fields import RGBColorField
from colorfield.fields import ColorField


class User(AbstractUser):
    organization = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=30, blank=True)



    class Meta:
        db_table = 'auth_user'


class Cluster(models.Model):
    cluster_name = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.cluster_name

    class Meta:
        db_table = 'clusters'


class Oblast(models.Model):

    oblast_name = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.oblast_name

    class Meta:
        managed = False
        db_table = 'oblasts'


class Raion(models.Model):
    raion_name = models.CharField(max_length=100)
    oblast = models.ForeignKey(Oblast)
    color = ColorField(default='#FF0000')
    # color = RGBColorField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.raion_name

    class Meta:
        db_table = 'raions'

class Settlement(models.Model):

    settlement_name = models.CharField(max_length=120)
    longitude = models.FloatField()
    latitude = models.FloatField()
    raion = models.ForeignKey(Raion)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.settlement_name

    class Meta:
        managed = False
        db_table = 'settlements'


class GCA_NGCA(models.Model):

    type_of_area = models.CharField(max_length=20)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.type_of_area

    class Meta:
        managed = False
        db_table = 'gca_ngca'


class NeedType(models.Model):
    need_type = models.CharField(max_length=50)

    def __unicode__(self):
        return self.need_type

    class Meta:
        # managed = False
        db_table = 'need_types'


class AffectedGroup(models.Model):
    affected_group_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.affected_group_name

    class Meta:
        managed = False
        db_table = 'affected_groups'


class AlertType(models.Model):
    alert_type = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.alert_type

    class Meta:
        managed = False
        db_table = 'alert_types'


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __unicode__(self):
        return self.status

    class Meta:
        managed = False
        db_table = 'status'


class ConfirmationStatus(models.Model):
    confirmation_status = models.CharField(max_length=30)

    def __unicode__(self):
        return self.confirmation_status

    class Meta:
        db_table = 'confirmation_status'

class OrganizationType(models.Model):

    type = models.CharField(max_length=80, null=True)

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'organization_types'


class Organization(models.Model):

    organization_name = models.CharField(max_length=80)
    organization_acronym = models.CharField(max_length=30, null=True)
    organization_type = models.ForeignKey(OrganizationType, null=True)

    def __unicode__(self):
        return '%s: %s' % (self.organization_acronym, self.organization_name)

    class Meta:
        db_table = 'organizations'
        ordering = ['organization_name']


class Alert(models.Model):

    oblast = models.ForeignKey(Oblast)
    raion = ChainedForeignKey(
        Raion,
        chained_field="oblast",
        chained_model_field="oblast",
        show_all=False,
        auto_choose=False,
        sort=True
    )
    date_referal = models.DateField(verbose_name='Date of Incident')
    informant = models.TextField(blank=True, null=True)

    referral_agency = models.ForeignKey(Organization, related_name='referral_agency_id')

    referral_agency.admin_order_field = 'organization_name'

    settlement = ChainedForeignKey(
        Settlement,
        chained_field="raion",
        chained_model_field="raion",
        show_all=False,
        auto_choose=False,
        sort=True
    )

    gca_ngca = models.ForeignKey(GCA_NGCA, verbose_name='GCA/NGCA')
    yes_no = (
        (0, 'No'),
        (1, 'Yes')
    )
    alert_type = models.ForeignKey(AlertType)
    conflict_related = models.IntegerField(
        choices=yes_no
    )

    description = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    affected = models.ForeignKey(AffectedGroup, related_name='affected_id', verbose_name='Affected group')
    source_info = models.CharField(max_length=255, blank=True, null=True)

    status = models.ForeignKey(Status)
    confirmation_status = models.ForeignKey(ConfirmationStatus, null=True, default=1)
    date_update = models.DateField(blank=True, null=True)


    additional_info_link = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    population = models.BigIntegerField(blank=True, null=True, verbose_name='Baseline population')

    population_males = models.BigIntegerField(blank=True, null=True)
    population_females = models.BigIntegerField(blank=True, null=True)
    population_children = models.BigIntegerField(blank=True, null=True)
    population_adult = models.BigIntegerField(blank=True, null=True)
    population_elderly = models.BigIntegerField(blank=True, null=True)

    no_affected = models.IntegerField(verbose_name='Number of affected (ind.)')

    no_affected_males = models.BigIntegerField(blank=True, null=True)
    no_affected_females = models.BigIntegerField(blank=True, null=True)
    no_affected_children = models.BigIntegerField(blank=True, null=True)
    no_affected_adult = models.BigIntegerField(blank=True, null=True)
    no_affected_elderly = models.BigIntegerField(blank=True, null=True)

    no_beneficiaries = models.IntegerField(blank=True, null=True, verbose_name='Number of beneficiaries')

    no_beneficiaries_males = models.BigIntegerField(blank=True, null=True)
    no_beneficiaries_females = models.BigIntegerField(blank=True, null=True)
    no_beneficiaries_children = models.BigIntegerField(blank=True, null=True)
    no_beneficiaries_adult = models.BigIntegerField(blank=True, null=True)
    no_beneficiaries_elderly = models.BigIntegerField(blank=True, null=True)

    clusters = models.ManyToManyField(Cluster, related_name='clusters_id')
    need_types = models.ManyToManyField(NeedType, related_name='needs')

    def location(self):
        location = ' / '.join([str(self.oblast), str(self.raion), str(self.settlement)])
        return location

    def __unicode__(self):
        return '%d affected in %s, %s raion (%s obl.)' % (self.no_affected, self.settlement, self.raion, self.oblast)

    location.admin_order_field = 'location'

    class Meta:
        db_table = 'alerts'


class ItemGroup(models.Model):

    item_group_name = models.CharField(max_length=80, blank=True, null=True)

    def __unicode__(self):
        return self.item_group_name

    class Meta:
        db_table = 'item_groups'

class Item(models.Model):

    item_name = models.CharField(max_length=80, blank=True, null=True)
    item_label_en = models.CharField(max_length=120, blank=True, null=True)
    item_label_ua = models.CharField(max_length=120, blank=True, null=True)
    item_label_ru = models.CharField(max_length=120, blank=True, null=True)
    item_group = models.ForeignKey(ItemGroup, null=True)

    def __unicode__(self):
        return self.item_name

    class Meta:
        db_table = 'items'


class Unit(models.Model):

    unit_name = models.CharField(max_length=15, blank=True, null=True)
    unit_label_en = models.CharField(max_length=30, blank=True, null=True)
    unit_label_ua = models.CharField(max_length=30, blank=True, null=True)
    unit_label_ru = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.unit_name

    class Meta:
        db_table = 'item_units'


class AlertItem(models.Model):

    alert = models.ForeignKey(Alert, related_name='items')
    item = models.ForeignKey(Item)
    item_details = models.CharField(max_length=120, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unit = models.ForeignKey(Unit)
    #
    # def __unicode__(self):
    #     return self.item_name

    class Meta:
        db_table = 'alert_items'


class Response(models.Model):

    response_partners = models.ManyToManyField(Organization, related_name='response_partners_id')
    item = models.ForeignKey(Item)
    item_details = models.CharField(max_length=120, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unit = models.ForeignKey(Unit)
    date = models.DateField(blank=True, null=True)
    alert = models.ForeignKey(Alert, related_name='responses', on_delete=models.CASCADE)
    uncovered_needs = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    response_partners.admin_order_field = 'organization_name'
    # def partners(self):
    #     return obj.

    class Meta:
        db_table='responses'