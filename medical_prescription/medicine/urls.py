from django.conf.urls import url
from .views import ListActivePrinciple, CreateCustomActivePrinciple

urlpatterns = (url(r'^list/$', ListActivePrinciple.as_view(), name='activeprinciple_list'),
               url(r'^create/$', CreateCustomActivePrinciple.as_view(), name='create_activePrinciple'),)
