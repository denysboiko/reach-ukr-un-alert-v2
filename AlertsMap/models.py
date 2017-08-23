from __future__ import unicode_literals
from django.core.urlresolvers import reverse
import urlparse
from django.db import models
from django.db.models import Max, Min, Sum
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import AbstractUser
from colorfield.fields import ColorField
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    organization = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=30, blank=True)


    class Meta:
        db_table = 'auth_user'

class Emails(models.Model):

    email = models.EmailField()

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'emails'
        verbose_name_plural = 'Emails'

class Cluster(models.Model):

    cluster_name = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.cluster_name

    class Meta:
        db_table = 'clusters'


class GCA_NGCA(models.Model):

    type_of_area = models.CharField(max_length=20)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.type_of_area

    class Meta:
        managed = False
        db_table = 'gca_ngca'


class Oblast(models.Model):
    pcode = models.CharField(max_length=10, blank=True, null=True)
    oblast_name = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.oblast_name

    class Meta:
        db_table = 'oblasts'


class Raion(models.Model):
    pcode = models.CharField(max_length=10, blank=True, null=True)
    raion_name = models.CharField(max_length=100)
    oblast = models.ForeignKey(Oblast)
    color = ColorField(default='#FF0000')
    # color = RGBColorField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.raion_name

    class Meta:
        db_table = 'raions'


class CoordinationHub(models.Model):

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    # to_list = models.ManyToManyField(Emails, related_name='to_emails')
    # cc_list = models.ManyToManyField(Emails, related_name='cc_emails')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'coordination_hubs'

class Settlement(models.Model):

    pcode = models.CharField(max_length=10, blank=True, null=True)
    pcode_new = models.CharField(max_length=10, blank=True, null=True)
    settlement_name_old = models.CharField(max_length=120, blank=True, null=True)
    settlement_name = models.CharField(max_length=120)
    longitude = models.FloatField()
    latitude = models.FloatField()
    raion = models.ForeignKey(Raion)
    area = models.ForeignKey(GCA_NGCA, blank=True, null=True)
    hub = models.ForeignKey(CoordinationHub, blank=True, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.settlement_name

    class Meta:
        db_table = 'settlements'





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


class ClusterEmail(models.Model):

    cluster = models.ForeignKey(Cluster)
    coordination_hub = models.ForeignKey(CoordinationHub)
    to_list = models.ManyToManyField(Emails, related_name='to_emails')
    cc_list = models.ManyToManyField(Emails, related_name='cc_emails')

    class Meta:
        db_table = 'cluster_emails'

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

    date_referal = models.DateField(verbose_name=_('Date of Incident'))
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

    gca_ngca = models.ForeignKey(GCA_NGCA, verbose_name=_('GCA/NGCA'))

    yes_no = (
        (0, _('No')),
        (1, _('Yes'))
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
        return '%s / %s / %s' % (self.raion, self.settlement, self.oblast)


    def related_to_conflict(self):
        return (_("No"), _("Yes"))[self.conflict_related]

    def edit_url(self):
        domain = Site.objects.get_current().domain
        slug = reverse('admin:AlertsMap_alert_change', args=(self.id,))
        url = domain + slug
        return url

    def view_url(self):
        domain = Site.objects.get_current().domain
        slug = urlparse.urljoin('/alert/', str(self.id))
        url = urlparse.urljoin(domain, slug)
        return url

    def get_clusters_list(self):
        query = Alert.objects.filter(pk=self.pk).prefetch_related('clusters').values('clusters__cluster_name')
        return map(lambda x: x['clusters__cluster_name'], query)

    def get_needs_list(self):
        query = Alert.objects.filter(pk=self.pk).prefetch_related('need_types').values('need_types__need_type')
        return map(lambda x: x['need_types__need_type'], query)

    def get_response_partners(self):
        res = Response.objects.filter(alert=self.pk).values('response_partners__organization_name').distinct()
        return map(lambda x: x['response_partners__organization_name'], res)

    def get_items(self):
        res = AlertItem.objects.filter(alert=self.pk).prefetch_related('item','unit').values('item__item_name','unit__unit_name').annotate(quantity_need=Sum('quantity'))
        return res

    def get_response_items(self):

        responses = Response.objects.filter(alert=self.pk).values('item__item_name', 'unit__unit_name').annotate(
            quantity_response=Sum('quantity'))

        res = {}

        for item in responses:
            name = item['item__item_name']
            res[name] = item['quantity_response']
        return res

    def get_recipients(self, cluster_ids):

        def get_mail_lists(id, cluster_ids):

            # mails_to = CoordinationHub.objects.filter(pk=id).prefetch_related('to_list').values_list('to_list__email')
            # mails_copy = CoordinationHub.objects.filter(pk=id).prefetch_related('cc_list').values_list('cc_list__email')
            #
            # copy = map(lambda x: x[0], mails_copy)
            # to = map(lambda x: x[0], mails_to)

            clusters_cc = map(lambda x: x[0], Cluster.objects.filter(pk__in=cluster_ids).prefetch_related('cc_list').values_list('cc_list__email'))
            clusters_to = map(lambda x: x[0], Cluster.objects.filter(pk__in=cluster_ids).prefetch_related('to_list').values_list('to_list__email'))

            emails_to = ClusterEmail.objects.filter(coordination_hub=id, cluster__in=cluster_ids).prefetch_related('to_list').values_list('to_list__email')
            emails_cc = ClusterEmail.objects.filter(coordination_hub=id, cluster__in=cluster_ids).prefetch_related('cc_list').values_list('cc_list__email')

            return {'To': map(lambda x: x[0], emails_to), 'CC': map(lambda x: x[0], emails_cc)}

        location_id = self.settlement.pk
        query = Settlement.objects.filter(pk=location_id).prefetch_related('hub').values('hub__id', 'settlement_name')
        responsible_hub = query[0]['hub__id']

        # clusters_cc = map(lambda x: x[0], self.clusters.prefetch_related('cc_list').values_list('cc_list__email'))
        # clusters_to = map(lambda x: x[0], self.clusters.prefetch_related('to_list').values_list('to_list__email'))
        # self.settlement.hub.to_list.prefetch_related('cc_emails').values('email')
        # self.settlement.hub.to_list.prefetch_related('to_emails').values('email')
        # obj.settlement.hub.to_list.prefetch_related('email').values('cc_emails__cc_list__email')
        # cluster_ids = map(lambda x : x[0], self.clusters.values_list('pk'))

        recipients = get_mail_lists(responsible_hub, cluster_ids)

        return recipients

    # def __unicode__(self):
    #     return _('%d affected in %s, %s raion (%s obl.)') % (self.no_affected, self.settlement, self.raion, self.oblast)

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

    item_name = models.CharField(max_length=120, blank=True, null=True)
    item_group = models.ForeignKey(ItemGroup, null=True)

    def __unicode__(self):
        return self.item_name

    class Meta:
        db_table = 'items'


class Unit(models.Model):

    unit_name = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.unit_name

    class Meta:
        db_table = 'item_units'


class AlertItem(models.Model):

    alert = models.ForeignKey(Alert, related_name='items')
    item = models.ForeignKey(Item)
    item_details = models.CharField(max_length=120, blank=True, null=True)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit)

    # def __unicode__(self):
    #     return self.item_name

    class Meta:
        db_table = 'alert_items'


class Response(models.Model):

    response_partners = models.ManyToManyField(Organization, related_name='response_partners_id')
    item = models.ForeignKey(Item)
    item_details = models.CharField(max_length=120, blank=True, null=True)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit)
    date = models.DateField(blank=True, null=True)
    alert = models.ForeignKey(Alert, related_name='responses', on_delete=models.CASCADE)
    uncovered_needs = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    response_partners.admin_order_field = 'organization_name'
    # def partners(self):
    #     return obj
    class Meta:
        db_table='responses'