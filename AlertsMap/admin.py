from django.contrib import admin
import json
from .models import *
# from moderation.admin import ModerationAdmin
from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.admin import UserAdmin
from guardian.admin import GuardedModelAdmin

# from django.contrib.auth.models import User

# admin.site.unregister(User)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'organization', 'phone', 'email', 'password1', 'password2',)
    }),
)


# UserAdmin.add_form = UserChangeFormExtended
# UserAdmin.add_fieldsets = (
#     (None, {
#         'classes': ('wide',),
#         'fields': ('username', 'organization', 'phone', 'email', 'password1', 'password2',)
#     }),
# )


admin.site.register(User, UserAdmin)

# ModelAdmin
# GuardedModelAdmin
# ModerationAdmin


def check_access(user, group):
    if user:
        return user.groups.filter(name=group).count() > 0
    return False


class ItemsInline(admin.TabularInline):
    model = AlertItem
    verbose_name = "Need by item"
    verbose_name_plural = "Need by item"
    extra = 1
    classes = ('collapse',)


class ResponsesInline(admin.StackedInline):

    model = Response
    verbose_name = "Response by item"
    verbose_name_plural = "Response by item"
    extra = 1

    fieldsets = (
        (None,  {
            # 'classes': ('collapse',),
            'fields': (
                ('item', 'item_details', 'quantity', 'unit'),
                ('response_partners'),
                ('action', 'uncovered_needs', 'date'),
                ('comments')
        )}),
    )

    filter_horizontal = ('response_partners',)


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
        (None, {'fields': (('action','uncovered_needs', 'date'),)}),
        (None, {'fields': ('comments',)})
    )

    filter_horizontal = ('response_partners',)

    def items(self, obj):
        return '%d %s of %s' % (obj.quantity, obj.unit, obj.item)


class AlertAdmin(ModelAdmin):

    list_filter = ['date_referal','oblast','confirmation_status']

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
        ('Population figures',{
            'classes': ('collapse',),
            'fields': (
                ('no_affected_males','no_beneficiaries_males','population_males'),
                ('no_affected_females','no_beneficiaries_females','population_females'),
                ('no_affected_children','no_beneficiaries_children','population_children'),
                ('no_affected_adult','no_beneficiaries_adult','population_adult'),
                ('no_affected_elderly','no_beneficiaries_elderly','population_elderly')
            )
        }),
        (None, {'fields': ()})
    )

    inlines = [ItemsInline, ResponsesInline]

    editor_fields = (

                ('need_types','clusters'),
                ('status','referral_agency'),
                ('date_referal'),
                ('informant','context'),
                ('description','comments'),
                'date_update'

            )

    moderation_fields = ('confirmation_status',)

    def get_form(self, request, obj=None, **kwargs):
        # request.user.is_superuser

        if check_access(request.user, 'Moderators') | request.user.is_superuser:
            self.fieldsets[2][1]['fields'] = self.editor_fields + self.moderation_fields

        else:
            self.fieldsets[2][1]['fields'] = self.editor_fields

        return super(AlertAdmin, self).get_form(request, obj, **kwargs)

    # filter_horizontal = ('response_partners',)

    actions = ['confirm_alerts', 'reject_alerts']

    def get_actions(self, request):
        actions = super(AlertAdmin, self).get_actions(request)
        if not (check_access(request.user, 'Moderators') | request.user.is_superuser):
            if 'confirm_alerts' in actions:
                del actions['confirm_alerts']
                del actions['reject_alerts']
        return actions

    # def get_object(self, request, object_id):
    #     obj = super(AlertAdmin, self).get_object(request, object_id)
    #     if obj is not None:
    #         obj.confirmation_status = 1
    #     return obj

    def confirm_alerts(self, request, queryset):
        queryset.update(confirmation_status=2)

    def reject_alerts(self, request, queryset):
        queryset.update(confirmation_status=3)

    confirm_alerts.short_description = "Confirm selected alerts"
    reject_alerts.short_description = "Reject selected alerts"

    def save_model(self, request, obj, form, change):
        new_data = form.__dict__['cleaned_data']

        obj.cluster =new_data['clusters'][0]
        # obj.response_partner = new_data['response_partners'][0]
        obj.need_type = new_data['need_types'][0]

        # print(form.__dict__['cleaned_data'])
        # if obj.new_data['clusters'] != 2:
        #     obj.confirmation_status = 1

        obj.save()

    class Media:
        css = {
            'screen': ('css/admin.css', 'css/selectize/selectize.css',)
        }
        js = (
            'js/jquery.min.js',
            # 'js/demo/sifter.min.js',
            'js/collapse_inlines.js',
            # 'js/collapsed_stacked_inlines.js',
            # 'js/selectize.min.js',

        )

class OrganizationAdmin(ModelAdmin):

    search_fields = ['organization_name','organization_acronym']

    list_display = ['organization_name','organization_acronym','organization_type']

admin.site.register([Cluster, Raion])
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Response, ResponseAdmin)