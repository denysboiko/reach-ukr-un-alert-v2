from django.shortcuts import render
from AlertsMap.models import Alert
from rest_framework import viewsets
from AlertsMap.forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from AlertsMap.serializers import AlertsSerializer

class AlertsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Alert.objects.all().values(
        'id',
        'date_referal',
        'settlement__settlement_name',
        'settlement__latitude',
        'settlement__longitude',

        'oblast__oblast_name',
        'raion__raion_name',
        'raion',

        'oblast',
        'settlement',

        'status',
        'cluster',
        'response_partner',

        'informant',
        'referral_agency',
        'conflict_related',
        'description',
        'context',
        'affected__affected_group_name',
        'no_affected',
        'status__status',
        'cluster__cluster_name',
        'alert_type__alert_type',
        'need_type__need_type',
        'source_info',
        'confirmation',
        'action',
        'no_beneficiaries',
        'date_update',
        'gap_beneficiaries',
        'uncovered_needs',
        'additional_info_link',
        'comments'

    )
    # .values('settlement')
    # .values('gca_ngca')
    # .values('settlement',)
    serializer_class = AlertsSerializer
    pagination_class = None

def home(request):
    return render(
        request,
        'index.html',
        {
            'user': request.user,
            'data': '../alerts/?format=json'
        }
    )

def test(request):
    return render(
        request,
        'index.html',
        {
            'user': request.user,
            'data': '../alerts/?format=json'
        }
    )


@csrf_protect
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')

    else:
        form = RegistrationForm()

    # variables = RequestContext(request, {
    #             'form': form
    #         })

    return render(request, 'registration/register.html', {'form': form})


def register_success(request):
    return render(
        request,
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')