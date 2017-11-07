# Django
from django.db import models

# Django Local
from prescription.models import Prescription


class PrescriptionRecommendation(models.Model):
    """
    Model to associate prescription to recommendation many to many cardinality.
    """
    prescription = models.ForeignKey(Prescription)
    recommendation = models.CharField(max_length=1000)
