from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from AlertsMap.views import *
from rest_framework import routers
from django.views.i18n import JavaScriptCatalog

router = routers.DefaultRouter()

router.register(r'clusters', ClustersViewSet)
router.register(r'response', ResponsePartnersViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'alerts', AlertViewSet, base_name='alerts-list')


js_info_dict = {
    'domain': 'djangojs',
    'packages': ('alerts_map',),
}

urlpatterns = [

    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^admin/logout/$', logout_page),
    url(r'^admin/login/$', auth_views.LoginView.as_view()),

    url(r'^admin/', admin.site.urls),

    url(r'^$', home),
    url(r'^alert/(?P<alert_id>\d+)/$', alert),
    url(r'^', include(router.urls)),
    url(r'^raions/$', RaionAutocomplete.as_view(), name='raions'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript_catalog'),
    url(r'^agnocomplete/', include(('agnocomplete.urls', 'agnocomplete'), namespace='reviews')),
    url(r'^grappelli/', include('grappelli.urls')),
]
