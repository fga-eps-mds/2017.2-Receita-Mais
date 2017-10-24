from django.db import models

from medicine.models import Medicine
from prescription.models import Prescription


class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(Prescription)
    medicine = models.ForeignKey(Medicine)
