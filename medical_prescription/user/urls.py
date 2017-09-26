# Django
from django.conf.urls import url
from user.views import (ConfirmPasswordView,
                        DeleteHealthProfessional,
                        LoginView,
                        LogoutView,
                        RegisterHealthProfessionalView,
                        RegisterPatientView,
                        ResetPasswordView,
                        ShowHomePageView,
                        ShowPatientsView,
                        ShowHealthProfessionalView,
                        UpdateHealthProfessional,
                        UpdatePatient
                        )


urlpatterns = (
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^reset/$', ResetPasswordView.as_view(), name='reset_password'),
    url(r'^reset_confirm/(?P<activation_key>\w+)/$', ConfirmPasswordView.as_view(), name='confirm_password'),
    url(r'^home/$', ShowHomePageView.as_view(), name='home'),
    url(r'^register_health_professional/$', RegisterHealthProfessionalView.as_view(), name='register'),
    url(r'^view_health_professional/$', ShowHealthProfessionalView.as_view(), name='view_health_professional'),
    url(r'^edit_health_professional/(?P<pk>[0-9]+)/$', UpdateHealthProfessional.as_view(), name='edit'),
    url(r'^delete_health_professional/(?P<pk>[0-9]+)/$', DeleteHealthProfessional.as_view(), name='delete'),
    url(r'^register_patient/$', RegisterPatientView.as_view(), name='register_patient'),
    url(r'^view_patient/$', ShowPatientsView.as_view(), name='view_patient'),
    url(r'^edit_patient/(?P<pk>[0-9]+)/$', UpdatePatient.as_view(), name='edit_patient'),
)
