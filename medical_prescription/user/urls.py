# Django
from django.conf.urls import url

# local Django
from . import views

urlpatterns = (
    url(r'^$', views.show_homepage, name='home'),

    url(r'^register_patient/$', views.register_patient, name='register_patient'),
    url(r'^view_patient/$', views.view_patient, name='view_patient'),
    url(r'^edit_patient/(?P<pk>[0-9]+)/$', views.UpdatePatient.as_view(), name='edit_patient'),
)
