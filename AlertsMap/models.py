from __future__ import unicode_literals

from django.db import models
from smart_selects.db_fields import ChainedForeignKey
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


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
        managed = False
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

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.raion_name

    class Meta:
        managed = False
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

    type_of_area = models.CharField(max_length=200)

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
        managed = False
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


class Alert(models.Model):
    # admin1 = models.CharField(max_length=10)
    # admin2 = models.CharField(max_length=10)
    # admin4 = models.CharField(max_length=10)
    # user_id = models.IntegerField(null=True)

    oblast = models.ForeignKey(Oblast)
    raion = ChainedForeignKey(
        Raion,
        chained_field="oblast",
        chained_model_field="oblast",
        show_all=False,
        auto_choose=False,
        sort=True
    )
    date_referal = models.DateField()
    informant = models.TextField(blank=True, null=True)
    referral_agency = models.TextField(blank=True, null=True)
    settlement = ChainedForeignKey(
        Settlement,
        chained_field="raion",
        chained_model_field="raion",
        show_all=False,
        auto_choose=False,
        sort=True
    )
    gca_ngca = models.ForeignKey(GCA_NGCA)
    yes_no = (
        (0, 'No'),
        (1, 'Yes')
    )
    alert_type = models.ForeignKey(AlertType)
    conflict_related = models.IntegerField(
        choices=yes_no
    )
    need_type = models.ForeignKey(NeedType)
    description = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    affected = models.ForeignKey(AffectedGroup)
    no_affected = models.IntegerField()
    source_info = models.CharField(max_length=255, blank=True, null=True)
    cluster = models.ForeignKey(Cluster)
    response_partner = models.CharField(max_length=255, blank=True, null=True)
    confirmation = models.IntegerField(
        choices=yes_no
    )
    action = models.CharField(max_length=255, blank=True, null=True)
    no_beneficiaries = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey(Status)
    date_update = models.DateField(blank=True, null=True)
    gap_beneficiaries = models.IntegerField(blank=True, null=True)
    uncovered_needs = models.CharField(max_length=255, blank=True, null=True)
    additional_info_link = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    # related_name = None, to_field = None

    class Meta:
        managed = False
        db_table = 'alerts'