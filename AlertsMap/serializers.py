from AlertsMap.models import Alert, Cluster, Organization, NeedType
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ClustersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cluster
        fields = ('cluster_name',)


class ResponsePartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('organization_name',)

class AlertsSerializer(serializers.ModelSerializer):

    settlement = serializers.ReadOnlyField(source='settlement.settlement_name')
    oblast = serializers.ReadOnlyField(source='oblast.oblast_name')
    raion = serializers.ReadOnlyField(source='raion.raion_name')
    raionCode = serializers.ReadOnlyField(source='raion.id')
    longitude = serializers.ReadOnlyField(source='settlement.longitude')
    latitude = serializers.ReadOnlyField(source='settlement.latitude')
    status = serializers.ReadOnlyField(source='status.status')
    cluster = serializers.ReadOnlyField(source='cluster.cluster_name')
    clusters = ClustersSerializer(many=True)
    type = serializers.ReadOnlyField(source='alert_type.alert_type')
    need = serializers.ReadOnlyField(source='need_type.need_type')
    response_partner = serializers.ReadOnlyField(source='response_partner.organization_name')

    # settlement = serializers.ReadOnlyField(source='settlement.settlement_name')

    response_partners = ResponsePartnersSerializer(many=True)
    # clusters = serializers.ReadOnlyField(source='clusters.cluster_name')

    class Meta:

        model = Alert

        fields = (
            'id',
            'settlement',
            'oblast',
            'raion',
            'raionCode',
            'latitude',
            'longitude',
            'no_affected',
            'date_referal',
            'status',
            'cluster',
            'clusters',
            'response_partner',
            'type',
            'need',
            'gap_beneficiaries',
            'context',
            'description',
            'population',
            'additional_info_link',
            'uncovered_needs',
            'conflict_related',

            'response_partners'
        )