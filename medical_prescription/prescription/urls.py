# Django
from django.conf.urls import url

# Local Django
from .views import (CreatePrescriptionView)


urlpatterns = (
    url(r'^$', CreatePrescriptionView.as_view(), name='create_prescription'),
)
