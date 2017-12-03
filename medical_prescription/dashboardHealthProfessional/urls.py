# Django
from django.conf.urls import url
from dashboardHealthProfessional.views import (Home,
                                               ChartData)


urlpatterns = (
    url(r'^health_professional/$', Home.as_view(), name='dashboard_hp'),
    url(r'^ajax/chart_data/$', ChartData.as_view(), name='chart_data')

)
