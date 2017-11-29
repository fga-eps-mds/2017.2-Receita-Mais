# Django
from django.conf.urls import url

# Local Django
from .views import (AutoCompleteExam,
                    AutoCompletePatient,
                    AutoCompleteCid,
                    OpenPrescriptionView,
                    AutoCompleteMedicine,
                    CreatePrescriptionView,
                    ShowDetailPrescriptionView,
                    ListFavoritePrescription,
                    FavoritePrescription,
                    ListPatientPrescription,
                    CreatePatternView,
                    ListPrescription,
                    CreateCopyPrescription,
                    ListPrescription,
                    PrintPrescription,
                    CreatePatternView,
                    ShowPatternsView,
                    SugestionsCid
                    )

urlpatterns = (
    url(r'^$', OpenPrescriptionView.as_view(), name='create_prescription'),
    url(r'^ajax/autocomplete_exam/$', AutoCompleteExam.as_view(), name='autocomplete_exam'),
    url(r'^ajax/autocomplete_cid/$', AutoCompleteCid.as_view(), name='autocomplete_cid'),
    url(r'^ajax/autocomplete_patient/$', AutoCompletePatient.as_view(), name='autocomplete_patient'),
    url(r'^ajax/autocomplete_medicine/$', AutoCompleteMedicine.as_view(),
        name='autocomplete_medicine'),
    url(r'^ajax/sugestions_cid/$', SugestionsCid.as_view(), name='sugestions_cid'),
    url(r'^create_modal/$', CreatePrescriptionView.as_view(), name='create_modal'),
    url(r'^list_prescription/$', ListPrescription.as_view(), name='list_prescription'),
    url(r'^list_prescription_patient/$', ListPatientPrescription.as_view(), name='list_patient_prescription'),
    url(r'^create_prescription_model/$', CreatePatternView.as_view(), name='create_prescription_model'),
    url(r'^favorite_prescription/(?P<pk>[0-9]+)/$', FavoritePrescription.as_view(), name='favorite_prescription'),
    url(r'^list_favorite_prescription/$', ListFavoritePrescription.as_view(), name='list_favorite_prescription'),
    url(r'^show_prescription/(?P<pk>[\w-]+)$', ShowDetailPrescriptionView.as_view(),
        name='show_prescription'),
    url(r'^create_copy_prescription/(?P<pk>[\w-]+)$', CreateCopyPrescription.as_view(),
        name='copy_prescription'),
    url(r'^show_patterns/(?P<pk>[\w-]+)$', ShowPatternsView.as_view(),
        name='show_patterns'),
    url(r'^print_prescription/(?P<pk>[0-9]+)/(?P<jk>[0-9]+)/$', PrintPrescription.generate_pdf,
        name='print_prescription'),
    )
