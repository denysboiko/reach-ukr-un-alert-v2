from AlertsMap.models import Alert
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AlertsSerializer(serializers.ModelSerializer):

    # HyperlinkedModelSerializer
    settlement = serializers.ReadOnlyField(source='settlement__settlement_name')
    oblast = serializers.ReadOnlyField(source='oblast__oblast_name')
    raion = serializers.ReadOnlyField(source='raion__raion_name')
    raionCode = serializers.ReadOnlyField(source='raion')
    longitude = serializers.ReadOnlyField(source='settlement__longitude')
    latitude = serializers.ReadOnlyField(source='settlement__latitude')
    status = serializers.ReadOnlyField(source='status__status')
    cluster = serializers.ReadOnlyField(source='cluster__cluster_name')
    type = serializers.ReadOnlyField(source='alert_type__alert_type')
    need = serializers.ReadOnlyField(source='need_type__need_type')

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
            'response_partner',
            'type',
            'need',
            'gap_beneficiaries',
            'context',
            'description',
            'additional_info_link',
            'uncovered_needs',
            'conflict_related'
        )
        # '__all__'
