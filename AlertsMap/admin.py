from AlertsMap.forms import RaionForm
from .models import *
from django.contrib.admin import AdminSite, ModelAdmin
from .mail import notify_mail

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from AlertsMap.translate import translate_text, translate_field

UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'organization', 'phone', 'email', 'password1', 'password2',)
    }),
)


def check_access(user, group):
    if user:
        return user.groups.filter(name=group).count() > 0
    return False


class ItemsInline(admin.StackedInline):
    model = AlertItem
    verbose_name = _("Need by items")
    verbose_name_plural = _("Needs by items")
    extra = 1
    classes = ('grp-collapse grp-open',)

    fieldsets = (
        (None, {
            'fields': (
                ('item', 'item_details', 'quantity', 'unit'),
                ('item_details_en', 'item_details_ru', 'item_details_uk')
            )}),
    )


class EmailsInline(admin.TabularInline):
    model = ClusterEmail
    verbose_name = _("Cluster recipient list")
    verbose_name_plural = _("Cluster recipient lists")
    extra = 0
    classes = 'collapse'


class CoordinationHubAdmin(ModelAdmin):
    inlines = [EmailsInline]


class ResponsesInline(admin.StackedInline):
    model = Response
    verbose_name = _("Response by items")
    verbose_name_plural = _("Responses by items")
    extra = 1
    classes = ('grp-collapse grp-open',)

    fieldsets = (
        (None, {
            'fields': (
                ('item', 'item_details', 'quantity', 'unit'),
                'response_partners'
            )}),
        (None, {
            'fields': (
                ('action', 'uncovered_needs', 'date'),
                'comments'
            )})
    )


class ResponseAdmin(ModelAdmin):

    list_display = [
        'item',
        'quantity',
        'unit',
        'date'
    ]

    fieldsets = (
        (None, {'fields': ('alert',)}),
        (None, {'fields': (
            ('item', 'item_details', 'quantity', 'unit'),
        )}),
        (None, {'fields': ('response_partners',)}),
        (None, {'fields': (('action', 'uncovered_needs', 'date'),)}),
        (None, {'fields': ('comments',)})
    )

    filter_horizontal = ('response_partners',)


class AlertAdmin(ModelAdmin):
    list_filter = ['date_referal', 'oblast', 'confirmation_status']

    list_display = [
        'location',
        'affected',
        'alert_type',
        'confirmation_status',
        'description',
        'date_referal'
    ]

    regular_fields = (
        (None, {'fields': (
            ('oblast', 'raion', 'settlement', 'gca_ngca'),
            ('affected', 'conflict_related', 'alert_type'),
            ('no_affected', 'no_beneficiaries', 'population')
        )}),
        (_('Population figures (by groups)'), {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                ('no_affected_males', 'no_beneficiaries_males', 'population_males'),
                ('no_affected_females', 'no_beneficiaries_females', 'population_females'),
                ('no_affected_children', 'no_beneficiaries_children', 'population_children'),
                ('no_affected_adult', 'no_beneficiaries_adult', 'population_adult'),
                ('no_affected_elderly', 'no_beneficiaries_elderly', 'population_elderly')
            )
        }),
        (None, {'fields': (
            ('need_types', 'clusters'),
            ('status', 'referral_agency'),
            ('date_referal',)
        )}),
        (None, {'fields': (('informant', 'context'),)}),
        (_('Translation'), {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                ('informant_en', 'context_en'),
                ('informant_uk', 'context_uk'),
                ('informant_ru', 'context_ru')
            )
        }),
        (None, {'fields': (('description', 'comments'),)}),
        (_('Translation'), {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                ('description_en', 'comments_en'),
                ('description_uk', 'comments_uk'),
                ('description_ru', 'comments_ru')
            )
        }),
        (None, {'fields': ('date_update',)})
    )

    moderation_fields = (None, {'fields': (('confirmation_status',))})

    fieldsets = regular_fields

    inlines = [ItemsInline, ResponsesInline]

    def get_form(self, request, obj=None, **kwargs):

        if check_access(request.user, 'Moderators') | request.user.is_superuser:
            self.fieldsets = self.regular_fields + (self.moderation_fields,)

        return super(AlertAdmin, self)\
            .get_form(request, obj, **kwargs)

    actions = ['confirm_alerts', 'reject_alerts']

    def get_actions(self, request):
        actions = super(AlertAdmin, self).get_actions(request)
        if not (check_access(request.user, 'Moderators') | request.user.is_superuser):
            if 'confirm_alerts' in actions:
                del actions['confirm_alerts']
                del actions['reject_alerts']
        return actions

    def confirm_alerts(self, request, queryset):
        queryset.update(confirmation_status=2)

    confirm_alerts.short_description = _("Confirm selected alerts")

    def reject_alerts(self, request, queryset):
        queryset.update(confirmation_status=3)

    reject_alerts.short_description = _("Reject selected alerts")

    def save_model(self, request, obj, form, change):

        new_data = form.__dict__['cleaned_data']
        obj.cluster = new_data['clusters'][0]
        obj.need_type = new_data['need_types'][0]

        clusters = []
        needs = []
        status = ''

        translate_field(obj, "informant")
        translate_field(obj, "context")
        translate_field(obj, "description")
        translate_field(obj, "comments")

        cluster_ids = map(lambda x: x.pk, new_data['clusters'])
        if not change:
            clusters = map(lambda x: x.cluster_name, new_data['clusters'])
            needs = map(lambda x: x.need_type, new_data['need_types'])
            status = 'New object'
        else:
            clusters = obj.get_clusters_list()
            needs = obj.get_needs_list()
            status = 'Changed object'

        obj.save()

        recipients = obj.get_recipients(cluster_ids)
        change_url = obj.edit_url()
        notify_mail(recipients['To'], recipients['CC'], obj, clusters, needs, change_url)

    def items(self, obj):
        return '%d affected in %s, %s raion (%s obl.)' % (obj.no_affected, obj.settlement, obj.raion, obj.oblast)

    class Media:
        css = {
            'screen': (
                'css/admin.css',
                'css/selectize/selectize.css',
                'css/selectize/selectize.default.min.css',
                'admin/selectize.css')
        }
        js = (
            'js/jquery.min.js',
            'admin/selectize.js',
            # 'js/demo/sifter.min.js',
            # 'js/collapse_inlines.js',
            # 'js/collapsed_stacked_inlines.js',
            'js/selectize.min.js',

        )


class OrganizationAdmin(ModelAdmin):
    search_fields = ['organization_name', 'organization_acronym']
    list_display = ['organization_name', 'organization_acronym', 'organization_type']


class RaionAdmin(ModelAdmin):
    list_filter = ['oblast']
    search_fields = ['raion_name', 'pcode']
    list_display = [
        'pcode',
        'raion_name',
        'oblast'
    ]


class SettlementAdmin(ModelAdmin):
    list_filter = ['area', 'raion']
    search_fields = ['settlement_name', 'pcode']
    list_display = [
        'pcode',
        'settlement_name',
        'raion',
        'area'
    ]


class MailConfigAdmin(ModelAdmin):
    list_display = [
        'from_email',
        'subject',
        'body'
    ]


admin.site.register(User, UserAdmin)
admin.site.register(MailConfig, MailConfigAdmin)
admin.site.register([Cluster, Emails])
admin.site.register(CoordinationHub, CoordinationHubAdmin)
admin.site.register(Raion, RaionAdmin)
admin.site.register(Settlement, SettlementAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Response, ResponseAdmin)
