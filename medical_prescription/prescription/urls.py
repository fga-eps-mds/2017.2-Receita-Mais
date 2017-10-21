# Django
from django.conf.urls import url

# Local Django
from .views import (CreatePrescriptionView,
                    AutoCompleteExam,
                    AutoCompletePatient,
                    AutoCompleteCid,
                    CreateTestePrescriptionView)


urlpatterns = (
    url(r'^$', CreatePrescriptionView.as_view(), name='create_prescription'),
    url(r'^ajax/autocomplete_exam/$', AutoCompleteExam.as_view(), name='autocomplete_exam'),
    url(r'^ajax/autocomplete_cid/$', AutoCompleteCid.as_view(), name='autocomplete_cid'),
    url(r'^ajax/autocomplete_patient/$', AutoCompletePatient.as_view(), name='autocomplete_patient'),
    url(r'^create_modal/$', CreateTestePrescriptionView.as_view(), name='create_modal')
)
