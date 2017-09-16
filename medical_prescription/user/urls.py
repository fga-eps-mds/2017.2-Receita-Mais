from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^register/$', views.register_health_professional),
    url(r'^view/$', views.view_health_professional),
    url(r'^edit/$', views.edit_health_professional),
    url(r'^delete/$', views.delete_health_professional),
)
