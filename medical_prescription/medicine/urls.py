from django.conf.urls import url
from .views import ListActivePrinciple

url(r'^list/$', ListActivePrinciple.as_view(), name='activePrinciple_list'),
