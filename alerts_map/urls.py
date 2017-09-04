from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from AlertsMap.views import *
from rest_framework import routers
from django.conf.urls.i18n import i18n_patterns

router = routers.DefaultRouter()
# router.register(r'alerts', AlertsViewSet)
router.register(r'clusters', ClustersViewSet)
router.register(r'response', ResponsePartnersViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'alerts', AlertViewSet, base_name='alerts-list')



js_info_dict = {
    'domain': 'djangojs',
    'packages': ('alerts_map',),
}

urlpatterns = [

    url(r'^logout/$', logout_page),
    url(r'^login/$', auth_views.login),
    url(r'^$', home),
    url(r'^alert/(?P<alert_id>\d+)/$', alert),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^register/success/$', register_success),
    url(r'^', include(router.urls)),
    url(r'^', include('smart_selects.urls')),
    url(
        r'^agnocomplete/',
        include('agnocomplete.urls', namespace='agnocomplete')),
]


urlpatterns += i18n_patterns(
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)