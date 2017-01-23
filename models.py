# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
    need_type = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    affected = models.CharField(max_length=255)
    no_affected = models.IntegerField()
    source_info = models.CharField(max_length=255, blank=True, null=True)
    cluster = models.CharField(max_length=255)
    response_partner = models.CharField(max_length=255, blank=True, null=True)
    confirmation = models.IntegerField()
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
    cluster_0 = models.ForeignKey('Clusters', models.DO_NOTHING, db_column='cluster_id', blank=True, null=True)  # Field renamed because of name conflict.
    gca_ngca_0 = models.ForeignKey('GcaNgca', models.DO_NOTHING, db_column='gca_ngca_id', blank=True, null=True)  # Field renamed because of name conflict.
    settlement_id = models.BigIntegerField(blank=True, null=True)
    oblast_0 = models.ForeignKey('Oblasts', models.DO_NOTHING, db_column='oblast_id', blank=True, null=True)  # Field renamed because of name conflict.
    raion_0 = models.ForeignKey('Raions', models.DO_NOTHING, db_column='raion_id', blank=True, null=True)  # Field renamed because of name conflict.
    conflict_related = models.IntegerField(blank=True, null=True)
    status_0 = models.ForeignKey('Status', models.DO_NOTHING, db_column='status_id', blank=True, null=True)  # Field renamed because of name conflict.
    need_type_0 = models.ForeignKey('NeedTypes', models.DO_NOTHING, db_column='need_type_id', blank=True, null=True)  # Field renamed because of name conflict.
    alert_type_0 = models.ForeignKey(AlertTypes, models.DO_NOTHING, db_column='alert_type_id', blank=True, null=True)  # Field renamed because of name conflict.
    affected_group = models.ForeignKey(AffectedGroups, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alerts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clusters(models.Model):
    cluster_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clusters'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GcaNgca(models.Model):
    type_of_area = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'gca_ngca'


class NeedTypes(models.Model):
    need_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'need_types'


class Oblasts(models.Model):
    oblast_name = models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'oblasts'


class Raions(models.Model):
    raion_name = models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)
    oblast = models.ForeignKey(Oblasts, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'raions'


class Settlements(models.Model):
    settlement_name = models.CharField(max_length=120)
    raion = models.ForeignKey(Raions, models.DO_NOTHING)
    longitude = models.FloatField()
    latitude = models.FloatField()
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'settlements'


class Status(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'status'
