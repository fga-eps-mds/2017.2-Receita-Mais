from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^reset/$', views.reset_password, name='reset_password'),
    url(r'^register/$', views.register_health_professional),
    url(r'^view/$', views.view_health_professional),
    url(r'^edit/$', views.edit_health_professional),
    url(r'^delete/$', views.delete_health_professional),
)
