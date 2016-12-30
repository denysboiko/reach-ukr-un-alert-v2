from __future__ import unicode_literals

from django.db import models


class Alerts(models.Model):
    user_id = models.IntegerField()
    date_referal = models.DateField()
    informant = models.TextField(blank=True, null=True)
    referral_agency = models.TextField(blank=True, null=True)
    oblast = models.CharField(max_length=255)
    admin1 = models.CharField(max_length=10)
    raion = models.CharField(max_length=255)
    admin2 = models.CharField(max_length=10)
    settlements = models.CharField(max_length=255)
    admin4 = models.CharField(max_length=10)
    gca_ngca = models.CharField(max_length=255, blank=True, null=True)
    alert_type = models.CharField(max_length=255)
    conflict_related = models.CharField(max_length=255, blank=True, null=True)
    need_type = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    affected = models.CharField(max_length=255)
    no_affected = models.IntegerField()
    source_info = models.CharField(max_length=255, blank=True, null=True)
    cluster = models.CharField(max_length=255)
    response_partner = models.CharField(max_length=255, blank=True, null=True)
    confirmation = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    no_beneficiaries = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    date_update = models.DateField(blank=True, null=True)
    gap_beneficiaries = models.IntegerField(blank=True, null=True)
    uncovered_needs = models.CharField(max_length=255, blank=True, null=True)
    additional_info_link = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'alerts'