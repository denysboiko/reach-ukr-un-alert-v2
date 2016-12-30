from AlertsMap.models import Alerts
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class AlertsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

