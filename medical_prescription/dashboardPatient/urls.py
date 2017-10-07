# Django
from django.conf.urls import url
from dashboardHealthProfessional.views import (home)


urlpatterns = (
    url(r'^patient/$', home, name='dashboard_hp'),

)
