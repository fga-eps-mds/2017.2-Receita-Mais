from django.conf.urls import url
from .views import ListActivePrinciple

urlpatterns = (url(r'^list/$', ListActivePrinciple.as_view(), name='activeprinciple_list'),)
