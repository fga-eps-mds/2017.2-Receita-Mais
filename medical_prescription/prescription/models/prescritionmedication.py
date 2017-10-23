from django.db import models

from medication.models import Medication
from prescription.models import Prescription


class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(Prescription)
    medication = models.ForeignKey(Medication)
