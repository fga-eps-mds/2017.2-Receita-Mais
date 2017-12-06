# Django
from django.db import models

# Local Django
from . import Prescription
from user.models import Patient
from user import constants


class PatientPrescription(Prescription):
    """
    Prescription model especialization with ForeignKey Patient association.
    """
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=constants.NAME_MAX_LENGHT)
