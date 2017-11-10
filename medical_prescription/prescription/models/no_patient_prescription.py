# Django
from django.db import models

# Local Django
from . import Prescription
from user import constants


class NoPatientPrescription(Prescription):
    """
    Prescription model especialization with no ForeignKey Patient association.
    """
    patient = models.CharField(blank=False, null=False, max_length=constants.NAME_MAX_LENGHT)
