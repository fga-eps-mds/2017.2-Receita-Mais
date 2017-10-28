from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include, url
from django.contrib import admin

from landing.views import home

urlpatterns = [
    url(r'^user/', include('user.urls')),
    url(r'^dashboard_health_professional/', include('dashboardHealthProfessional.urls')),
    url(r'^medicine/', include('medicine.urls')),
    url(r'^dashboard_patient/', include('dashboardPatient.urls')),
    url(r'^exam/', include('exam.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^disease/', include('disease.urls')),
    url(r'^$', home, name='landing_page'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^prescription/', include('prescription.urls')),
    url(r'^chat/', include('chat.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^user/', include('user.urls')),
    url(r'^dashboard_health_professional/', include('dashboardHealthProfessional.urls')),
    url(r'^medicine/', include('medicine.urls')),
    url(r'^dashboard_patient/', include('dashboardPatient.urls')),
    url(r'^exam/', include('exam.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^disease/', include('disease.urls')),
    url(r'^prescription/', include('prescription.urls')),
    url(r'^chat/', include('chat.urls')),
    url(r'^$', home, name='landing_page'),
)
