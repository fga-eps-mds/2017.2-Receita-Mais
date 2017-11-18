# Django
from django.conf.urls import url

# Local Django
from .views import (AutoCompleteExam,
                    AutoCompletePatient,
                    AutoCompleteCid,
                    OpenPrescriptionView,
                    AutoCompleteMedicine,
                    CreatePrescriptionView,
                    ListPrescription,
                    printprescription,
                    CreatePatternView)

urlpatterns = (
    url(r'^$', OpenPrescriptionView.as_view(), name='create_prescription'),
    url(r'^ajax/autocomplete_exam/$', AutoCompleteExam.as_view(), name='autocomplete_exam'),
    url(r'^ajax/autocomplete_cid/$', AutoCompleteCid.as_view(), name='autocomplete_cid'),
    url(r'^ajax/autocomplete_patient/$', AutoCompletePatient.as_view(), name='autocomplete_patient'),
    url(r'^ajax/autocomplete_medicine/$', AutoCompleteMedicine.as_view(),
        name='autocomplete_medicine'),
    url(r'^create_modal/$', CreatePrescriptionView.as_view(), name='create_modal'),
    url(r'^list_prescription/$', ListPrescription.as_view(), name='list_prescription'),
    url(r'^print_prescription/(?P<pk>[0-9]+)/$', printprescription.generate_pdf, name='print_prescription'),
    url(r'^create_prescription_model/$', CreatePatternView.as_view(), name='create_prescription_model'),
    )
