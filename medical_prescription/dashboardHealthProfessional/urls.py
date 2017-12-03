# Django
from django.conf.urls import url
from dashboardHealthProfessional.views import (HomeHealthProfessional,
                                               ChartData)


urlpatterns = (
    url(r'^health_professional/$', HomeHealthProfessional.as_view(), name='dashboard_hp'),
    url(r'^ajax/chart_data/$', ChartData.as_view(), name='chart_data')

)
