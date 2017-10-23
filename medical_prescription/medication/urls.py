from django.conf.urls import url
from .views import (
                    ListManipulatedMedicinenByHealthProfessional,
                    ListAllMedicines,
                    CreateMedicineView,
                    UpdateMedicine)

urlpatterns = [
    url(r'^list_manipulated_medicines/$', ListManipulatedMedicinenByHealthProfessional.as_view(),
        name='list_manipulated_medicines'),
    url(r'^list_all_medicines/$', ListAllMedicines.as_view(), name='list_all_medicines'),
    url(r'^create_medicine/$', CreateMedicineView.as_view(), name='create_medicine'),
    url(r'^edit_medicine/(?P<pk>[\w-]+)$', UpdateMedicine.as_view(), name='edit_medicine'),
]
