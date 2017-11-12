# Django
from django.db import models

# Django Local
from medicine.models import Medicine
from prescription.models import Prescription
from prescription import constants


class PrescriptionHasMedicine(models.Model):
    """
    Model to associate prescription to medicine many to many cardinality.
    """
    posology = models.CharField(max_length=constants.MAX_LENGTH_POSOLOGY)
    quantity = models.IntegerField(choices=constants.QUANTITY_CHOICES)
    via = models.CharField(default=constants.VIA_CHOICES[0][0], blank=False, max_length=constants.MAX_LENGTH_VIA)
    prescription_medicine = models.ForeignKey(Prescription)
    medicine = models.ForeignKey(Medicine)
