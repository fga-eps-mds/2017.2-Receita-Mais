# Django
from django.conf.urls import url
from dashboardPatient.views import (HomePatient,
                                   )

urlpatterns = (
    url(r'^patient/$', HomePatient.as_view(), name='dashboard_patient'),
)
