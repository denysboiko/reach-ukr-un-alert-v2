from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from AlertsMap.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alerts', AlertsViewSet)
router.register(r'clusters', ClustersViewSet)
router.register(r'response', ResponsePartnersViewSet)
router.register(r'responses', ResponseViewSet)


urlpatterns = [
    url(r'^$', home),
    url(r'^test/$', test),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout_page),
    url(r'^login/$', auth_views.login),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^', include(router.urls)),
    url(r'^', include('smart_selects.urls')),
    url(
        r'^agnocomplete/',
        include('agnocomplete.urls', namespace='agnocomplete')),
]