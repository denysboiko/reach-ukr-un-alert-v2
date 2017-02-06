from django.contrib import admin
from .models import Alert, User, Cluster, BaselinePopulation
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




# class UserCreationFormExtended(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserCreationFormExtended, self).__init__(*args, **kwargs)
#         self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)
#         self.fields['organization'] = forms.CharField(label=_("Organization"), max_length=75)
#         self.fields['phone'] = forms.CharField(label=_("Phone"), max_length=75)
#
# class UserChangeFormExtended(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserChangeFormExtended, self).__init__(*args, **kwargs)
#         self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)
#         self.fields['organization'] = forms.CharField(label=_("Organization"), max_length=75)
#         self.fields['phone'] = forms.CharField(label=_("Phone"), max_length=75)
#
# UserAdmin.add_form = UserCreationFormExtended
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


class PopulationInline(admin.TabularInline):
    model = BaselinePopulation


# class ResponsePartnersInline(admin.StackedInline):
#     model = Alert
#


class AlertAdmin(ModelAdmin):

    list_filter = ['date_referal','oblast', 'confirmation_status']

    list_display = [
        'location',
        'affected',
        'cluster',
        'alert_type',
        'need_type',
        'confirmation_status',
        'description'
    ]

    fieldsets = (
        (None, {'fields': (
            ('oblast', 'raion', 'settlement', 'gca_ngca'),
            ('affected', 'conflict_related', 'alert_type'),
            ('no_affected', 'no_beneficiaries', 'gap_beneficiaries', 'population')
        )}),
        ('Population figures',{
            'classes': ('collapse',),
            'fields': (
                ('no_affected_males','no_beneficiaries_males','gap_beneficiaries_males','population_males'),
                ('no_affected_females','no_beneficiaries_females','gap_beneficiaries_females','population_females'),
                ('no_affected_children','no_beneficiaries_children','gap_beneficiaries_children','population_children'),
                ('no_affected_adult','no_beneficiaries_adult','gap_beneficiaries_adult','population_adult'),
                ('no_affected_elderly','no_beneficiaries_elderly','gap_beneficiaries_elderly','population_elderly')
            )
        }),
        (None, {'fields': ()})
    )

    editor_fields = (

                ('need_types','need_type'),
                ('clusters', 'cluster'),
                ('response_partners','response_partner'),
                ('status','action','uncovered_needs'),
                ('referral_agency','date_referal'),
                # ('source_info','additional_info_link'),
                'informant',
                'context',
                'description',
                'comments',
                'date_update'

            )

    moderation_fields = ('confirmation_status',)

    # inlines = [
    #     PopulationInline,
    # ]
    def get_form(self, request, obj=None, **kwargs):
        # request.user.is_superuser

        if check_access(request.user, 'Moderators') | request.user.is_superuser:
            self.fieldsets[2][1]['fields'] = self.editor_fields + self.moderation_fields

        else:
            self.fieldsets[2][1]['fields'] = self.editor_fields

        return super(AlertAdmin, self).get_form(request, obj, **kwargs)

    filter_horizontal = ('response_partners',)

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

    # fields = [
    #     'oblast',
    #     'raion',
    #     'settlement',
    #     'gca_ngca',
    #     'conflict_related',
    #     'alert_type',
    #     'cluster',
    #     'need_type',
    #     'affected',
    #     'date_referal',
    #     'date_update',
    #     'source_info',
    #     'confirmation',
    #     'informant',
    #     'no_affected',
    #     'no_beneficiaries',
    #     'gap_beneficiaries',
    #     'response_partner',
    #     'referral_agency',
    #     'description',
    #     'context',
    #     'action',
    #     'status',
    #     'uncovered_needs',
    #     'comments',
    #     'additional_info_link'
    # ]




admin.site.register(Alert, AlertAdmin)
admin.site.register(Cluster)