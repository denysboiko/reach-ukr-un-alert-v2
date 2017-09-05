from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from AlertsMap.models import *
from AlertsMap.forms import *
import json
from AlertsMap.serializers import *


from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers


from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny
from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response as RESTResponse
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse

User = get_user_model()

from django.utils import translation


class ClustersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = ClustersSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class ResponsePartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = ResponsePartnersSerializer


class ResponseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class AlertsViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = (AllowAny,)
    serializer_class = AlertsSerializer
    queryset = Alert.objects.filter(confirmation_status=2).values()
    pagination_class = None


def home(request):

    queryset = list(Raion.objects.values('id', 'raion_name', 'color', 'oblast'))

    return render(
        request,
        'index.html',
        {
            'user': request.user,
            'access': 1 if request.user.is_staff else 0,
            'new_alert': reverse('admin:AlertsMap_alert_add'),
            'data': '../alerts/?format=json',
            'raions': json.dumps(queryset)
        }
    )


def alert(request, **kwargs):

    id = kwargs.pop('alert_id')
    queryset = Alert.objects.filter(confirmation_status=2, pk = id).all()

    # data = serializers.serialize('json', queryset)
    return render(
        request,
        'alert.html',
        {
            'user': request.user,
            'alerts': queryset
        }
    )


def check_access(user):
    if user:
        return user.groups.filter(name='Staff').count() > 0
    return False



# class AlertViewSet(viewsets.ReadOnlyModelViewSet):
#
#     permission_classes = (AllowAny,)
#     serializer_class = AlertsSerializer
#     queryset = Alert.objects.filter(confirmation_status=2)
#     pagination_class = None
#
#     def get_serializer(self, *args, **kwargs):
#
#         hide = ('response_partners',)
#         alert = self.get_object
#
#         return self.serializer(alert, hide=hide, many=True)

class AlertViewSet(viewsets.ViewSet):

    """
    A simple ViewSet for listing or retrieving alert.
    """

    permission_classes = (AllowAny,)

    def list(self, request):

        hide = ('response_partners','context','description')
        if request.user.is_staff:
            hide = ()
            # print 'Listing view. User has access to see response partners'


        queryset = Alert.objects.filter(confirmation_status=2).all()
        serializer = AlertsSerializer(queryset, hide=hide, many=True)

        return RESTResponse(serializer.data)

    def retrieve(self, request, pk=None):

        hide = ('response_partners',)
        if request.user.is_staff:
            hide = None
            # print 'Detailed view. User has access to see response partners'

        queryset = Alert.objects.filter(confirmation_status=2).all()
        alert = get_object_or_404(queryset, pk=pk)
        serializer = AlertsSerializer(alert, hide=hide)

        return RESTResponse(serializer.data)



@csrf_protect
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                organization=form.cleaned_data['organization'],
                phone=form.cleaned_data['phone']
            )
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/")
            # return HttpResponseRedirect('/register/success/')

    else:
        form = RegistrationForm()

    # variables = RequestContext(request, {
    #             'form': form
    #         })

    return render(request, 'registration/register.html', {'form': form})


def register_success(request):
    return HttpResponseRedirect('/')
    # return render(
    #     request,
    #     'registration/success.html',
    # )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
