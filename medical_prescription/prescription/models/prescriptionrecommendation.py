from django.db import models

from prescription.models import Prescription


class PrescriptionRecommendation(models.Model):
    prescription = models.ForeignKey(Prescription)
    recommendation = models.CharField(max_length=1000)
