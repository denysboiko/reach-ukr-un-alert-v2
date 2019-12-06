from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class AlertSystemConfig(AppConfig):
    name = 'AlertsMap'
    verbose_name = _('Alert System')
