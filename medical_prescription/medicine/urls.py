# Django
from django.conf.urls import url
# Views app
from .views import (
                    ListAllPrinciple,
                    ListCustomPrinciple,
                    CreateCustomActivePrinciple,
                    EditCustomActivePrinciple,
                    ListManipulatedMedicinenByHealthProfessional,
                    ListAllMedicines,
                    CreateMedicineView,
                    UpdateMedicine)

urlpatterns = (url(r'^list_all_principle/$', ListAllPrinciple.as_view(), name='list_all_principle'),
               url(r'^list_custom_principle/$', ListCustomPrinciple.as_view(), name='list_custom_principle'),
               url(r'^create/$', CreateCustomActivePrinciple.as_view(), name='create_activePrinciple'),
               url(r'^edit_principle/(?P<pk>[0-9]+)/$', EditCustomActivePrinciple.as_view(), name='edit_principle'),
               url(r'^list_manipulated_medicines/$', ListManipulatedMedicinenByHealthProfessional.as_view(),
                   name='list_manipulated_medicines'),
               url(r'^list_all_medicines/$', ListAllMedicines.as_view(), name='list_all_medicines'),
               url(r'^create_medicine/$', CreateMedicineView.as_view(), name='create_medicine'),
               url(r'^edit_medicine/(?P<pk>[\w-]+)$', UpdateMedicine.as_view(), name='edit_medicine'),)
