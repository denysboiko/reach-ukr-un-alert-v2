from __future__ import unicode_literals
from django.urls import reverse
from urllib.parse import urljoin
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractUser
from colorfield.fields import ColorField
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from django.db.models import F


class User(AbstractUser):

    organization = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Emails(models.Model):

    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'emails'
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')


class Cluster(models.Model):

    cluster_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cluster_name

    class Meta:
        db_table = 'clusters'
        verbose_name = _('Cluster')
        verbose_name_plural = _('Clusters')

# GcaNgca
# GCA_NGCA
class GCA_NGCA(models.Model):

    type_of_area = models.CharField(max_length=20)

    def __str__(self):
        return self.type_of_area

    class Meta:
        db_table = 'gca_ngca'


class Oblast(models.Model):
    pcode = models.CharField(max_length=10, blank=True, null=True)
    oblast_name = models.CharField(max_length=100)

    def __str__(self):
        return self.oblast_name

    class Meta:
        db_table = 'oblasts'
        verbose_name = _('Oblast')
        verbose_name_plural = _('Oblasts')


class Raion(models.Model):

    pcode = models.CharField(max_length=10, blank=True, null=True)
    raion_name = models.CharField(max_length=100, verbose_name=_('Raion Name'))
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE, verbose_name=_('Oblast'))
    color = ColorField(default='#FF0000', verbose_name=_('Color'))

    def __str__(self):
        return self.raion_name

    class Meta:
        db_table = 'raions'
        verbose_name = _('Raion')
        verbose_name_plural = _('Raions')


class CoordinationHub(models.Model):

    name = models.CharField(max_length=50, verbose_name=_("Hub"))
    location = models.CharField(max_length=25, verbose_name=_("Location"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'coordination_hubs'
        verbose_name = _('Coordination hub')
        verbose_name_plural = _('Coordination hubs')


class Settlement(models.Model):

    pcode = models.CharField(max_length=12, blank=True, null=True)
    pcode_new = models.CharField(max_length=10, blank=True, null=True)
    settlement_name_old = models.CharField(max_length=120, blank=True, null=True,
                                           verbose_name=_('Settlement Name (old)'))
    settlement_name = models.CharField(max_length=120, verbose_name=_('Settlement Name'))
    longitude = models.FloatField()
    latitude = models.FloatField()
    raion = models.ForeignKey(Raion, on_delete=models.CASCADE, verbose_name=_('Raion'))
    area = models.ForeignKey(GCA_NGCA, blank=True, null=True, on_delete=models.CASCADE,
                             verbose_name=_('GCA/NGCA'))
    hub = models.ForeignKey(CoordinationHub, blank=True, null=True, on_delete=models.CASCADE,
                            verbose_name=_('Hub'))

    def __str__(self):
        return self.settlement_name

    class Meta:
        db_table = 'settlements'
        verbose_name = _("Settlement")
        verbose_name_plural = _("Settlements")


class NeedType(models.Model):
    need_type = models.CharField(max_length=50)

    def __str__(self):
        return self.need_type

    class Meta:
        db_table = 'need_types'
        verbose_name = _('Need Type')
        verbose_name_plural = _('Need Types')


class AffectedGroup(models.Model):
    affected_group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.affected_group_name

    class Meta:
        db_table = 'affected_groups'
        verbose_name = _('Affected Group')
        verbose_name_plural = _('Affected Groups')


class AlertType(models.Model):
    alert_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.alert_type

    class Meta:
        db_table = 'alert_types'
        verbose_name = _('Alert Type')
        verbose_name_plural = _('Alert Types')


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'status'
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')


class ConfirmationStatus(models.Model):
    confirmation_status = models.CharField(max_length=30)

    def __str__(self):
        return self.confirmation_status

    class Meta:
        db_table = 'confirmation_status'


class OrganizationType(models.Model):

    type = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'organization_types'


class Organization(models.Model):

    organization_name = models.CharField(max_length=80, verbose_name=_('Organization Name'))
    organization_acronym = models.CharField(max_length=30, null=True, verbose_name=_('Organization Acronym'))
    organization_type = models.ForeignKey(OrganizationType, null=True, on_delete=models.CASCADE,
                                          verbose_name=_('Organization Type'))

    def __str__(self):
        return '%s: %s' % (self.organization_acronym, self.organization_name)

    class Meta:
        db_table = 'organizations'
        ordering = ['organization_name']
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')


class ClusterEmail(models.Model):

    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    coordination_hub = models.ForeignKey(CoordinationHub, on_delete=models.CASCADE)
    to_list = models.ManyToManyField(Emails, related_name='to_emails', verbose_name=_("To List"))
    cc_list = models.ManyToManyField(Emails, related_name='cc_emails', verbose_name=_("Cc List"))

    class Meta:
        db_table = 'cluster_emails'


class Alert(models.Model):

    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE, verbose_name=_('Oblast'))
    raion = models.ForeignKey(Raion, on_delete=models.CASCADE, verbose_name=_('Raion'))
    date_referal = models.DateField(verbose_name=_('Date of Incident'))
    informant = models.TextField(blank=True, null=True, verbose_name=_('Informant'))
    referral_agency = models.ForeignKey(Organization, related_name='referral_agency_id', on_delete=models.CASCADE,
                                        verbose_name=_('Referral Agency'))
    referral_agency.admin_order_field = 'organization_name'
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, verbose_name=_('Settlement'))
    gca_ngca = models.ForeignKey(GCA_NGCA, on_delete=models.CASCADE, verbose_name=_('GCA/NGCA'))
    yes_no = (
        (0, _('No')),
        (1, _('Yes'))
    )
    alert_type = models.ForeignKey(AlertType, on_delete=models.CASCADE, verbose_name=_('Alert Type'))
    conflict_related = models.IntegerField(choices=yes_no, verbose_name=_('Conflict related'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    context = models.TextField(blank=True, null=True, verbose_name=_('Context'))
    affected = models.ForeignKey(AffectedGroup, related_name='affected_id', verbose_name=_('Affected Group'),
                                 on_delete=models.CASCADE)
    source_info = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name=_('Status'))
    confirmation_status = models.ForeignKey(ConfirmationStatus, null=True, default=1, on_delete=models.CASCADE,
                                            verbose_name=_('Confirmation Status'))
    date_update = models.DateField(blank=True, null=True, verbose_name=_('Date Updated'))
    additional_info_link = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True, verbose_name=_('Comments'))

    population = models.BigIntegerField(blank=True, null=True, verbose_name=_('Baseline Population'))
    population_males = models.BigIntegerField(blank=True, null=True, verbose_name=_('Population (male)'))
    population_females = models.BigIntegerField(blank=True, null=True, verbose_name=_('Population (female)'))
    population_children = models.BigIntegerField(blank=True, null=True, verbose_name=_('Population (children)'))
    population_adult = models.BigIntegerField(blank=True, null=True, verbose_name=_('Population (adult)'))
    population_elderly = models.BigIntegerField(blank=True, null=True, verbose_name=_('Population (elderly)'))

    no_affected = models.IntegerField(verbose_name=_('Number of Affected'))
    no_affected_males = models.BigIntegerField(blank=True, null=True, verbose_name=_('Number of Affected (male)'))
    no_affected_females = models.BigIntegerField(blank=True, null=True, verbose_name=_('Number of Affected (female)'))
    no_affected_children = models.BigIntegerField(blank=True, null=True,
                                                  verbose_name=_('Number of Affected (children)'))
    no_affected_adult = models.BigIntegerField(blank=True, null=True, verbose_name=_('Number of Affected (adult)'))
    no_affected_elderly = models.BigIntegerField(blank=True, null=True, verbose_name=_('Number of Affected (elderly)'))

    no_beneficiaries = models.IntegerField(blank=True, null=True, verbose_name=_('Number of Beneficiaries'))
    no_beneficiaries_males = models.BigIntegerField(blank=True, null=True,
                                                    verbose_name=_('Number of Beneficiaries (male)'))
    no_beneficiaries_females = models.BigIntegerField(blank=True, null=True,
                                                      verbose_name=_('Number of Beneficiaries (female)'))
    no_beneficiaries_children = models.BigIntegerField(blank=True, null=True,
                                                       verbose_name=_('Number of Beneficiaries (children)'))
    no_beneficiaries_adult = models.BigIntegerField(blank=True, null=True,
                                                    verbose_name=_('Number of Beneficiaries (adult)'))
    no_beneficiaries_elderly = models.BigIntegerField(blank=True, null=True,
                                                      verbose_name=_('Number of Beneficiaries (elderly)'))

    clusters = models.ManyToManyField(Cluster, related_name='clusters_id', verbose_name=_('Clusters'))
    need_types = models.ManyToManyField(NeedType, related_name='needs', verbose_name=_('Need Types'))

    def location(self):
        return '%s / %s / %s' % (self.raion, self.settlement, self.oblast)

    def related_to_conflict(self):
        return (_("No"), _("Yes"))[self.conflict_related]

    def edit_url(self):
        domain = Site.objects.get_current().domain
        slug = reverse('admin:AlertsMap_alert_change', args=(self.id,))
        url = urljoin(domain, slug)
        return url

    def view_url(self):
        domain = Site.objects.get_current().domain
        slug = urljoin('/alert/', str(self.id))
        url = urljoin(domain, slug)
        return url

    def get_clusters_list(self):
        lang = get_language()
        query = Alert.objects.filter(pk=self.pk).prefetch_related('clusters').values('clusters__cluster_name' + '_'
                                                                                     + lang)
        return map(lambda x: x['clusters__cluster_name' + '_' + lang], query)

    def get_needs_list(self):
        lang = get_language()
        query = Alert.objects.filter(pk=self.pk).prefetch_related('need_types').values('need_types__need_type' + '_'
                                                                                       + lang)
        return map(lambda x: x['need_types__need_type' + '_' + lang], query)

    def get_response_partners(self):
        lang = get_language()
        res = Response.objects.filter(alert=self.pk)\
            .values('response_partners__organization_name' + '_' + lang)\
            .distinct()

        return map(lambda x: x['response_partners__organization_name' + '_' + lang], res)

    def get_items(self):

        lang = get_language()
        item_name_field = 'item__item_name' + '_' + lang
        unit_name_field = 'unit__unit_name' + '_' + lang

        res = AlertItem.objects.filter(alert=self.pk)\
            .prefetch_related('item', 'unit') \
            .annotate(item_name=F(item_name_field), unit_name=F(unit_name_field)) \
            .values('item_name', 'unit_name') \
            .annotate(quantity_need=Sum('quantity'))
        return res

    def get_response_items(self):

        lang = get_language()
        item_name_field = 'item__item_name' + '_' + lang
        unit_name_field = 'unit__unit_name' + '_' + lang

        responses = Response.objects.filter(alert=self.pk)\
            .annotate(item_name=F(item_name_field), unit_name=F(unit_name_field))\
            .values('item_name', 'unit_name')\
            .annotate(quantity_response=Sum('quantity'))

        res = dict()

        for item in responses:
            name = item['item_name']
            res[name] = item['quantity_response']
        return res

    def get_recipients(self, cluster_ids):

        def get_mail_lists(hub_id, cluster_ids_list):

            emails_to = ClusterEmail.objects.filter(coordination_hub=hub_id, cluster__in=cluster_ids_list)\
                .prefetch_related('to_list').values_list('to_list__email')

            emails_cc = ClusterEmail.objects.filter(coordination_hub=hub_id, cluster__in=cluster_ids_list)\
                .prefetch_related('cc_list').values_list('cc_list__email')

            return {'To': map(lambda x: x[0], emails_to), 'CC': map(lambda x: x[0], emails_cc)}

        location_id = self.settlement.pk
        query = Settlement.objects.filter(pk=location_id).prefetch_related('hub').values('hub__id', 'settlement_name')
        responsible_hub = query[0]['hub__id']

        recipients = get_mail_lists(responsible_hub, cluster_ids)

        return recipients

    def __str__(self):
        return _('%(no_affected)d affected in %(settlement)s, %(raion)s raion (%(oblast)s obl.)') % {
            'no_affected': self.no_affected,
            'settlement': self.settlement,
            'raion': self.raion,
            'oblast': self.oblast
        }

    location.admin_order_field = 'location'

    class Meta:
        db_table = 'alerts'
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')


class ItemGroup(models.Model):

    item_group_name = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.item_group_name

    class Meta:
        db_table = 'item_groups'


class Item(models.Model):

    item_name = models.CharField(max_length=120, blank=True, null=True, verbose_name=_('Item Name'))
    item_group = models.ForeignKey(ItemGroup, null=True, on_delete=models.CASCADE, verbose_name=_('Item Group'))

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = 'items'


class Unit(models.Model):

    unit_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=_('Unit'))

    def __str__(self):
        return self.unit_name

    class Meta:
        db_table = 'item_units'


class AlertItem(models.Model):

    alert = models.ForeignKey(Alert, related_name='items', on_delete=models.CASCADE, verbose_name=_('Alert'))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('Item'))
    item_details = models.CharField(max_length=120, blank=True, null=True, verbose_name=_('Item Details'))
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('Unit'))

    def __str__(self):
        return _('%(quantity)d %(unit)s of %(item)s') % {
            'quantity': self.quantity,
            'unit': self.unit,
            'item': self.item
        }

    class Meta:
        db_table = 'alert_items'


class Response(models.Model):

    response_partners = models.ManyToManyField(Organization, related_name='response_partners_id',
                                               verbose_name=_('Response Partners'))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('Item'))
    item_details = models.CharField(max_length=120, blank=True, null=True, verbose_name=_('Item Details'))
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('Unit'))
    date = models.DateField(blank=True, null=True, verbose_name=_('Date'))
    alert = models.ForeignKey(Alert, related_name='responses', on_delete=models.CASCADE, verbose_name=_('Alert'))
    uncovered_needs = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Uncovered Needs'))
    action = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Action'))
    comments = models.TextField(blank=True, null=True, verbose_name=_('Comments'))

    response_partners.admin_order_field = 'organization_name'

    def __str__(self):
        return _('%(quantity)d %(unit)s of %(item)s') % {
            'quantity': self.quantity,
            'unit': self.unit,
            'item': self.item
        }

    class Meta:
        db_table = 'responses'
        verbose_name = _('Response')
        verbose_name_plural = _('Responses')


class MailConfig(models.Model):

    from_email = models.EmailField(verbose_name=_('From'))
    subject = models.CharField(max_length=200, verbose_name=_('Subject'))
    body = models.TextField(verbose_name=_('Body'))

    class Meta:
        db_table = 'mail_config'
        verbose_name = _('Mail Template')
        verbose_name_plural = _('Mail Templates')


class MapConfig(models.Model):

    zoom = models.IntegerField()
    min_zoom = models.IntegerField()
    max_zoom = models.IntegerField()
