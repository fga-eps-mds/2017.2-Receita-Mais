from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$', views.ResetPasswordView.as_view(), name='reset_password'),
    url(r'^register/$', views.register_view, name='register_view'),
    url(r'^view/$', views.view_health_professional),
    url(r'^edit/$', views.edit_health_professional),
    url(r'^delete/$', views.delete_health_professional),
    url(r'^reset_confirm/(?P<activation_key>\w+)/$', views.ConfirmPasswordView.as_view(), name='confirm_password'),
)
