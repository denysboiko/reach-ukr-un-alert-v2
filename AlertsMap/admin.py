from django.contrib import admin
import json
from .models import *
from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.admin import UserAdmin
from guardian.admin import GuardedModelAdmin
from mail import notify_mail
# from django.contrib.auth.models import User

# admin.site.unregister(User)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mail import notify_mail

UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'organization', 'phone', 'email', 'password1', 'password2',)
    }),
)


# ModelAdmin
# GuardedModelAdmin
# ModerationAdmin


def check_access(user, group):
    if user:
        return user.groups.filter(name=group).count() > 0
    return False


class ItemsInline(admin.TabularInline):
    model = AlertItem
    verbose_name = _("Need by items")
    verbose_name_plural = _("Needs by items")
    extra = 1
    classes = ('grp-collapse grp-open',)



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
    # list_filter = ['']
    list_display = [
        'items',
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

    def items(self, obj):
        return '%d %s of %s' % (obj.quantity, obj.unit, obj.item)


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

    fieldsets = (
        (None, {'fields': (
            ('oblast', 'raion', 'settlement', 'gca_ngca'),
            ('affected', 'conflict_related', 'alert_type'),
            ('no_affected', 'no_beneficiaries', 'population')
        )}),
        (_('Population figures'), {
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
        ('Translation', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                ('informant_en', 'context_en'),
                ('informant_uk', 'context_uk'),
                ('informant_ru', 'context_ru')
            )
        }),
        (None, {'fields': (('description', 'comments'),)}),
        ('Translation', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                ('description_en', 'comments_en'),
                ('description_uk', 'comments_uk'),
                ('description_ru', 'comments_ru')
            )
        }),
        (None, {'fields': ('date_update',)})
    )

    inlines = [ItemsInline, ResponsesInline]

    moderation_fields = (None, {'fields': (('confirmation_status',))})

    def get_form(self, request, obj=None, **kwargs):

        if check_access(request.user, 'Moderators') | request.user.is_superuser:
            self.fieldsets = self.fieldsets + ((self.moderation_fields,))

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

    confirm_alerts.short_description = "Confirm selected alerts"

    def reject_alerts(self, request, queryset):
        queryset.update(confirmation_status=3)

    reject_alerts.short_description = "Reject selected alerts"

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
            'screen': ('css/admin.css', 'css/selectize/selectize.css',)
        }
        js = (
            'js/jquery.min.js',
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


admin.site.register(User, UserAdmin)
admin.site.register([Cluster, Emails])
admin.site.register(CoordinationHub, CoordinationHubAdmin)
admin.site.register(Raion, RaionAdmin)
admin.site.register(Settlement, SettlementAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Response, ResponseAdmin)
