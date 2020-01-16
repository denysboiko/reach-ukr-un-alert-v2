from .models import *
from django.contrib.auth.models import User, Group
from django.core import serializers as django_serializers
from rest_framework import serializers


from django.db.models import Max, Min, Sum

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        hide = kwargs.pop('hide', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if hide is not None:
            # Drop any fields that are specified in the `hide` argument.
            disallowed = set(hide)
            existing = set(self.fields.keys())

            for field_name in disallowed:
                self.fields.pop(field_name)


class ClustersSerializer(serializers.ModelSerializer):

    key = serializers.ReadOnlyField(source='cluster_name')

    class Meta:
        model = Cluster
        fields = ('key',)


class ResponsePartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ('id', 'organization_name',)


class NeedItemsPartnersSerializer(serializers.ModelSerializer):

    item = serializers.StringRelatedField()
    unit = serializers.StringRelatedField()

    class Meta:
        model = AlertItem
        fields = ('item','quantity','unit')


class ResponseItemsPartnersSerializer(serializers.ModelSerializer):

    item = serializers.StringRelatedField()
    unit = serializers.StringRelatedField()

    class Meta:
        model = Response
        fields = ('item','quantity','unit')

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

class AlertsSerializer(DynamicFieldsModelSerializer):

    pcode = serializers.ReadOnlyField(source='settlement.id')
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
    response_partners = serializers.ReadOnlyField(source='get_response_partners')
    edit_url = serializers.ReadOnlyField()
    view_url = serializers.ReadOnlyField()
    items = serializers.ReadOnlyField(source='get_items')
    responses = serializers.ReadOnlyField(source='get_response_items')
    conflict_related = serializers.ReadOnlyField(source='get_conflict_related_display')

    class Meta:

        model = Alert
        fields = (
            'id',
            'pcode',
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
            'type',
            'need',
            'need_types',
            'context',
            'description',
            'population',
            'additional_info_link',
            'conflict_related',
            'response_partners',
            'items',
            'responses',
            'edit_url',
            'view_url'
        )