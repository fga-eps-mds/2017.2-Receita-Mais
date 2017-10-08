# Django
from django.conf.urls import url
from dashboardPatient.views import (home)


urlpatterns = (
    url(r'^patient/$', home, name='dashboard_hp'),

)
