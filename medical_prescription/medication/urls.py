from django.conf.urls import url
from .views import (
                    ListManipulatedMedicinenByHealthProfessional,
                    ListAllMedications,
                    CreateMedicationView,
                    UpdateMedication)

urlpatterns = [
    url(r'^list_medication/$', .as_view(), name='list_medication'),
    url(r'^list_all_medications/$', ListAllMedications.as_view(), name='list_all_medications'),
    url(r'^create_medication/$', CreateMedicationView.as_view(), name='create_medication'),
    url(r'^edit_medication/(?P<pk>[\w-]+)$', UpdateMedication.as_view(), name='edit_medication'),
]
