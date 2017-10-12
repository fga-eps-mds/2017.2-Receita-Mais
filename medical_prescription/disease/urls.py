from django.conf.urls import url
from .views import ListDisease

urlpatterns = (
    url(r'^list_disease/$', ListDisease.as_view(), name='disease_list'),
)
