from django.contrib import admin
from .models import Alert
from moderation.admin import ModerationAdmin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = Profile

    fields = [
        'organization',
        'phone'
    ]

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.register(User, UserProfileAdmin)


# class MyAdminSite(AdminSite):
#     site_header = 'Alerts Map Administration'

class AlertAdmin(ModerationAdmin):
    # ModerationAdmin
    # admin.ModelAdmin
    list_filter = ['date_referal','oblast']
    list_display = [
        'oblast',
        'affected',
        'alert_type',
        'need_type'
    ]

    fields = [
        'oblast',
        'raion',
        'settlement',
        'gca_ngca',
        'conflict_related',
        'alert_type',
        'cluster',
        'need_type',
        'affected',
        'date_referal',
        'date_update',
        'source_info',
        'confirmation',
        'informant',
        'no_affected',
        'no_beneficiaries',
        'gap_beneficiaries',
        'response_partner',
        'referral_agency',
        'description',
        'context',
        'action',
        'status',
        'uncovered_needs',
        'comments',
        'additional_info_link'
    ]

admin.site.register(Alert, AlertAdmin)