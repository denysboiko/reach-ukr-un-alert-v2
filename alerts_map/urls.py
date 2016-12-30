from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from AlertsMap.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alerts', AlertsViewSet)

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls))
]