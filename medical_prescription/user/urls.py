from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^register/$', views.register_health_professional, name='register'),
    url(r'^view/$', views.view_health_professional, name='view'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.UpdateHealthProfessional.as_view(), name='edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteHealthProfessional.as_view(), name='delete'),
)
