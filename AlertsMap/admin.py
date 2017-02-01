from django.contrib import admin
from .models import Alert, User
from moderation.admin import ModerationAdmin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin

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

class AlertAdmin(ModerationAdmin):

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