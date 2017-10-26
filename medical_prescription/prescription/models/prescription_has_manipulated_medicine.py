from django.db import models

from medicine.models import ManipulatedMedicine
from prescription.models import PrescriptionMedicine
from prescription import constants


class PrescriptionHasManipulatedMedicine(models.Model):
    posology = models.CharField(max_length=constants.MAX_LENGTH_POSOLOGY)
    quantity = models.IntegerField(choices=constants.QUANTITY_CHOICES)
    prescription_medicine = models.ForeignKey(PrescriptionMedicine)
    manipulated_medicine = models.ForeignKey(ManipulatedMedicine)
