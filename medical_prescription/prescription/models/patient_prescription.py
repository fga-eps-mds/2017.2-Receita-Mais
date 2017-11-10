# Django
from django.db import models

# Local Django
from . import Prescription
from user.models import Patient


class PatientPrescription(Prescription):
    """
    Prescription model especialization with ForeignKey Patient association.
    """
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE)
