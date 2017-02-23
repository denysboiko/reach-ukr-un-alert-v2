from .models import *
from django.contrib.auth.models import User, Group
from django.core import serializers as django_serializers
from rest_framework import serializers


class ClustersSerializer(serializers.ModelSerializer):

    key = serializers.ReadOnlyField(source='cluster_name')

    class Meta:
        model = Cluster
        fields = ('key',)


class ResponsePartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'organization_name',)


class ResponseSerializer(serializers.ModelSerializer):

    response_partners = serializers.StringRelatedField(many=True)
    # response_partners = ResponsePartnersSerializer(many=True)
    class Meta:
        model = Response
        fields = '__all__'


class AlertResponsePartnersSerializer(serializers.ModelSerializer):

    response_partners = serializers.StringRelatedField(many=True)

    class Meta:
        model = Response
        fields = ('response_partners',)


class ResponsePartnersField(serializers.Field):
    def get_attribute(self, obj):
        return obj

    def to_representation(self, obj):
        res = Response.objects.filter(alert=obj.pk).values('response_partners__organization_name').distinct()
        partners = []
        for partner in res:
             partners.append(partner['response_partners__organization_name'])
        return partners


class AlertsSerializer(serializers.ModelSerializer):

    settlement = serializers.ReadOnlyField(source='settlement.settlement_name')
    oblast = serializers.ReadOnlyField(source='oblast.oblast_name')
    raion = serializers.ReadOnlyField(source='raion.raion_name')
    raionCode = serializers.ReadOnlyField(source='raion.id')
    longitude = serializers.ReadOnlyField(source='settlement.longitude')
    latitude = serializers.ReadOnlyField(source='settlement.latitude')
    status = serializers.ReadOnlyField(source='status.status')
    cluster = serializers.ReadOnlyField(source='cluster.cluster_name')
    clusters = serializers.StringRelatedField(many=True)
    type = serializers.ReadOnlyField(source='alert_type.alert_type')
    need = serializers.ReadOnlyField(source='need_type.need_type')
    need_types = serializers.StringRelatedField(many=True)
    response_partner = serializers.ReadOnlyField(source='response_partner.organization_name')
    # responses = ResponseSerializer(many=True)
    # response_partners = ResponsePartnersField(many=True, source='responses', read_only=True)
    response_partners = ResponsePartnersField()
    # response_partners = AlertResponsePartnersSerializer(many=True, source='responses')

    # serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # ReadOnlyField(source='alert__responses__item_id')
    # response_partners = ResponsePartnersSerializer(many=True)
    # tracks = serializers.SlugRelatedField(
    #     many=True
    #     read_only=True,
    #     slug_field='title'
    # )

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
            'no_beneficiaries',
            'date_referal',
            'status',
            'cluster',
            'clusters',
            'response_partner',
            'type',
            'need',
            'need_types',
            'context',
            'description',
            'population',
            'additional_info_link',
            'uncovered_needs',
            'conflict_related',
            'response_partners'
        )