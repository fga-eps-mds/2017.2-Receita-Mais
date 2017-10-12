from django.conf.urls import url
from .views import ListMedicationByHealthProfessional

urlpatterns = [
    url(r'^list_medication/$', ListMedicationByHealthProfessional.as_view(), name='list_medication'),
]
