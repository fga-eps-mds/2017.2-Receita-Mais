from django.conf.urls import include, url
from django.contrib import admin

from landing.views import home

urlpatterns = [
    url(r'^user/', include('user.urls')),
    url(r'^dashboard_health_professional/', include('dashboardHealthProfessional.urls')),
    url(r'^medicine/', include('medicine.urls')),
    url(r'^medication/', include('medication.urls')),
    url(r'^dashboard_patient/', include('dashboardPatient.urls')),
    url(r'^exam/', include('exam.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='landing_page'),
]
