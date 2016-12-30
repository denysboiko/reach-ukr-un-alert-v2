from django.shortcuts import render
from AlertsMap.models import Alerts
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from AlertsMap.serializers import AlertsSerializer

class AlertsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer

def home(request):
    return render(
        request,
        'index.html',
        { 'user': request.user
        }
    )