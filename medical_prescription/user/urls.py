# Django
from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$', views.ResetPasswordView.as_view(), name='reset_password'),
    url(r'^view/$', views.view_health_professional),
    url(r'^reset_confirm/(?P<activation_key>\w+)/$', views.ConfirmPasswordView.as_view(), name='confirm_password'),
    url(r'^home/$', views.show_homepage, name='home'),
    url(r'^register_health_professional/$', views.register_health_professional, name='register'),
    url(r'^view_health_professional/$', views.view_health_professional, name='view'),
    url(r'^edit_health_professional/(?P<pk>[0-9]+)/$', views.UpdateHealthProfessional.as_view(), name='edit'),
    url(r'^delete_health_professional/(?P<pk>[0-9]+)/$', views.DeleteHealthProfessional.as_view(), name='delete'),
    url(r'^register_patient/$', views.register_patient, name='register_patient'),
    url(r'^view_patient/$', views.view_patient, name='view_patient'),
    url(r'^edit_patient/(?P<pk>[0-9]+)/$', views.UpdatePatient.as_view(), name='edit_patient'),
)
