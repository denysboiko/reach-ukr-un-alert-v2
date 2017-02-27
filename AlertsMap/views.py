from django.shortcuts import render

from AlertsMap.models import *
from AlertsMap.forms import *

from AlertsMap.serializers import *

from rest_framework import viewsets

from django.contrib.auth.decorators import login_required, user_passes_test

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.permissions import AllowAny

from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, get_user_model
User = get_user_model()



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

    queryset = Alert.objects.filter(confirmation_status=2)

    permission_classes = (AllowAny,)
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
