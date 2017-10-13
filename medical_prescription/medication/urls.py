from django.conf.urls import url

from .views import ListMedicationByHealthProfessional, ListAllMedications

urlpatterns = [
    url(r'^list_medication/$', ListMedicationByHealthProfessional.as_view(), name='list_medication'),
    url(r'^list_all_medications/$', ListAllMedications.as_view(), name='list_all_medications'),
]
