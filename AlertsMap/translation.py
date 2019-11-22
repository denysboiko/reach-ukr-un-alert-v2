from modeltranslation.translator import register, translator, TranslationOptions
from .models import *


@register(Unit)
class UnitTranslation(TranslationOptions):
    fields = ('unit_name',)


@register(Item)
class UnitTranslation(TranslationOptions):
    fields = ('item_name',)


@register(Cluster)
class ClusterTranslationOptions(TranslationOptions):
    fields = ('cluster_name',)


@register(CoordinationHub)
class ClusterTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Oblast)
class OblastTranslation(TranslationOptions):
    fields = ('oblast_name',)


@register(GCA_NGCA)
class GcaNgcaTranslation(TranslationOptions):
    fields = ('type_of_area',)


@register(Raion)
class RaionTranslation(TranslationOptions):
    fields = ('raion_name',)


@register(Settlement)
class SettlementTranslation(TranslationOptions):
    fields = ('settlement_name',)


@register(NeedType)
class NeedTypeTranslation(TranslationOptions):
    fields = ('need_type',)


@register(AffectedGroup)
class AffectedGroupTranslation(TranslationOptions):
    fields = ('affected_group_name',)


@register(AlertType)
class AlertTypeTranslation(TranslationOptions):
    fields = ('alert_type',)


@register(Status)
class StatusTranslation(TranslationOptions):
    fields = ('status',)


@register(ConfirmationStatus)
class ConfirmationStatusTranslation(TranslationOptions):
    fields = ('confirmation_status',)


@register(OrganizationType)
class OrganizationTypeTranslation(TranslationOptions):
    fields = ('type',)


@register(Organization)
class OrganizationTranslation(TranslationOptions):
    fields = ('organization_name', 'organization_acronym')
