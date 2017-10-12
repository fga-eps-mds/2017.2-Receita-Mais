from django.conf.urls import url

from .views import ListMedication

urlpatterns = [
    url(r'^list_medication/$', ListMedication.as_view(), name='list_medication'),
]
