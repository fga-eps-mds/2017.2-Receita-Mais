# Django
from django.conf.urls import url
from django.contrib.auth.decorators import permission_required

# Local Django
from user.views import (ConfirmPasswordView,
                        DeleteHealthProfessional,
                        EditProfileView,
                        LogoutView,
                        LoginView,
                        RegisterPatientView,
                        RegisterHealthProfessionalView,
                        ResetPasswordView,
                        ShowHomePageView,
                        ShowPatientsView,
                        ShowHealthProfessionalView,
                        UpdateHealthProfessional,
                        UpdatePatient,
                        ConfirmAccountView,
                        UpdateUserPassword,
                        AddPatientView,
                        ListLinkedPatientsView
                        )


urlpatterns = (
    url(r'^login_patient/$', LoginView.as_view(), name='login_patient'),
    url(r'^login_healthprofessional/$', LoginView.as_view(), name='login_healthprofessional'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^reset/$', ResetPasswordView.as_view(), name='reset_password'),
    url(r'^reset_confirm/(?P<activation_key>\w+)/$', ConfirmPasswordView.as_view(), name='confirm_password'),
    url(r'^home/$', ShowHomePageView.as_view(), name='home'),
    url(r'^register_health_professional/$', RegisterHealthProfessionalView.as_view(), name='register'),
    url(r'^view_health_professional/$', permission_required('is_staff')(ShowHealthProfessionalView.as_view()), name='view_health_professional'),
    url(r'^edit_health_professional/(?P<pk>[0-9]+)/$', UpdateHealthProfessional.as_view(), name='edit'),
    url(r'^delete_health_professional/(?P<pk>[0-9]+)/$', DeleteHealthProfessional.as_view(), name='delete'),
    url(r'^register_patient/(?P<activation_key>\w+)/$', RegisterPatientView.as_view(), name='register_patient'),
    url(r'^view_patient/$', permission_required('is_staff')(ShowPatientsView.as_view()), name='view_patient'),
    url(r'^edit_profile/$', EditProfileView.as_view(), name='edit_profile'),
    url(r'^edit_patient/(?P<pk>[0-9]+)/$', UpdatePatient.as_view(), name='edit_patient'),
    url(r'^confirm/(?P<activation_key>\w+)/$', ConfirmAccountView.activate_register_user, name='confirm_account'),
    url(r'^editpasswordpatient/(?P<email>[\w|\W]+)/$', UpdateUserPassword.edit_patient_password_view, name='edit_patient_password'),
    url(r'^editpasswordhealthprofessional/(?P<email>[\w|\W]+)/$', UpdateUserPassword.edit_health_professional_password_view, name='edit_hp_password'),
    url(r'^addpatient/$', AddPatientView.as_view(), name='add_patient'),
    url(r'^listlinkedpatients/$', ListLinkedPatientsView.as_view(), name='list_linked_patients')
)
