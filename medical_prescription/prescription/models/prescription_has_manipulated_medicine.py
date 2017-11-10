# Django
from django.db import models

# Django Local
from medicine.models import ManipulatedMedicine
from prescription.models import Prescription
from prescription import constants


class PrescriptionHasManipulatedMedicine(models.Model):
    """
    Model to associate prescription to manipulated medicine many to many cardinality.
    """
    posology = models.CharField(max_length=constants.MAX_LENGTH_POSOLOGY)
    quantity = models.IntegerField(choices=constants.QUANTITY_CHOICES)
    via = models.CharField(default=constants.VIA_CHOICES[0][0], blank=False, max_length=constants.MAX_LENGTH_VIA)
    prescription_medicine = models.ForeignKey(Prescription)
    manipulated_medicine = models.ForeignKey(ManipulatedMedicine)
