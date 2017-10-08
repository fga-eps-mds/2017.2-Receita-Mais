# Django
from django.conf.urls import url
from dashboardHealthProfessional.views import (home)


urlpatterns = (
    url(r'^health_professional/$', home, name='dashboard_hp'),

)
