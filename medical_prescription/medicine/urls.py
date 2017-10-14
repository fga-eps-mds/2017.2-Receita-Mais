# Django
from django.conf.urls import url
# Views app
from .views import ListActivePrinciple, CreateCustomActivePrinciple, EditCustomActivePrinciple

urlpatterns = (url(r'^list/$', ListActivePrinciple.as_view(), name='activeprinciple_list'),
               url(r'^create/$', CreateCustomActivePrinciple.as_view(), name='create_activePrinciple'),
               url(r'^edit/(?P<pk>[0-9]+)/$', EditCustomActivePrinciple.as_view(), name='edit_activePrinciple'),)
